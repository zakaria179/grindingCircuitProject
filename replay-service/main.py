import os
import glob
import time
import json
import csv
import sys
import paho.mqtt.client as mqtt

MQTT_BROKER = os.getenv("MQTT_BROKER", "mosquitto")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
TOPIC_TELEMETRY = "ocp/grinding/telemetry"
REPLAY_INTERVAL = float(os.getenv("REPLAY_INTERVAL", 1.0))

def connect_mqtt():
    client = mqtt.Client(client_id="syscad_replay_service")
    connected = False
    while not connected:
        try:
            print(f"[replay-service] Connecting to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}...", flush=True)
            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            client.loop_start()
            connected = True
            print("[replay-service] Connected successfully to Mosquitto MQTT broker.", flush=True)
        except Exception as e:
            print(f"[replay-service] Mosquitto connection pending ({e}). Retrying in 3 seconds...", flush=True)
            time.sleep(3)
    return client

def find_csv_file():
    csv_files = glob.glob("*.csv") + glob.glob("data/*.csv")
    if csv_files:
        return csv_files[0]
    return None

def main():
    print("=== OCP Grinding Circuit — SysCAD CSV Replay Service ===", flush=True)
    client = connect_mqtt()

    while True:
        csv_path = find_csv_file()
        if not csv_path:
            print("[replay-service] No CSV file found in /replay-service folder yet.", flush=True)
            print("[replay-service] Please place your SysCAD CSV export file inside /replay-service.", flush=True)
            time.sleep(5)
            continue

        print(f"[replay-service] Found SysCAD CSV file: {csv_path}. Starting telemetry replay...", flush=True)
        try:
            with open(csv_path, mode='r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                row_count = 0
                for row in reader:
                    row_count += 1
                    payload = {
                        "sequence": row_count,
                        "timestamp": row.get("timestamp") or row.get("Timestamp") or time.time(),
                        "telemetry": row
                    }
                    json_data = json.dumps(payload)
                    client.publish(TOPIC_TELEMETRY, json_data)
                    
                    # Also publish by equipment tag if present in row
                    for equip in ["PB_001", "SP_001", "BM_001", "CY_001"]:
                        equip_data = {k: v for k, v in row.items() if equip.lower() in k.lower()}
                        if equip_data:
                            client.publish(f"ocp/grinding/equipment/{equip}", json.dumps({
                                "equipment_id": equip,
                                "timestamp": payload["timestamp"],
                                "metrics": equip_data
                            }))

                    print(f"[replay-service] Replayed row {row_count} -> MQTT topic: {TOPIC_TELEMETRY}", flush=True)
                    time.sleep(REPLAY_INTERVAL)

                print(f"[replay-service] Completed full cycle of {row_count} readings. Re-starting replay loop...", flush=True)
        except Exception as e:
            print(f"[replay-service] Error reading CSV file: {e}. Retrying in 5 seconds...", flush=True)
            time.sleep(5)

if __name__ == "__main__":
    main()
