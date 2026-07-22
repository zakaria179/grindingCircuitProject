import os
import glob
import time
import json
import csv
import paho.mqtt.client as mqtt

MQTT_BROKER = os.getenv("MQTT_BROKER", "mosquitto")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
TOPIC_TELEMETRY = "ocp/grinding/telemetry"
REPLAY_INTERVAL = float(os.getenv("REPLAY_INTERVAL", 1.0))

EQUIPMENT_MAPPINGS = {
    "Slurry_In": ["Feed Solid Flow", "Feed BPL", "Feed P80", "Feed Solid Fraction"],
    "PB_001": ["Feed Solid Flow", "Cyclone Underflow Solid Flow", "Process Water Solid Flow"],
    "SP_001": ["Cyclone Feed Solid Flow", "Cyclone Feed BPL", "Cyclone Feed P80", "Cyclone Feed Solid Fraction"],
    "CY_001": ["Cyclone Feed Solid Flow", "Cyclone Underflow Solid Flow", "Cyclone Underflow P80", "Output Slurry P80"],
    "BM_001": ["Ball Mill Discharge Solid Flow", "Ball Mill Discharge BPL", "Ball Mill Discharge P80", "Ball Mill Discharge Solid Fraction"],
    "Slurry_Out": ["Output Slurry Solid Flow", "Output Slurry BPL", "Output Slurry P80", "Output Slurry Solid Fraction"]
}

def connect_mqtt():
    if hasattr(mqtt, "CallbackAPIVersion"):
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="syscad_replay_service")
    else:
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
            time.sleep(5)
            continue

        print(f"[replay-service] Processing SysCAD dataset '{csv_path}'...", flush=True)
        try:
            with open(csv_path, mode='r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                row_count = 0
                for row in reader:
                    row_count += 1
                    
                    # Convert numerical fields to float/int if possible
                    parsed_metrics = {}
                    for k, v in row.items():
                        if k is None:
                            continue
                        clean_key = k.strip()
                        try:
                            parsed_metrics[clean_key] = float(v)
                        except (ValueError, TypeError):
                            parsed_metrics[clean_key] = v

                    record_no = parsed_metrics.get("RecordNo", row_count)
                    time_str = parsed_metrics.get("Time", "")
                    elapsed_hrs = parsed_metrics.get("ElapsedHrs", 0)

                    payload = {
                        "record_no": record_no,
                        "time": time_str,
                        "elapsed_hrs": elapsed_hrs,
                        "timestamp": time.time(),
                        "telemetry": parsed_metrics
                    }
                    
                    # 1. Publish master telemetry
                    client.publish(TOPIC_TELEMETRY, json.dumps(payload))

                    # 2. Publish targeted equipment topics
                    for equip_id, keys in EQUIPMENT_MAPPINGS.items():
                        equip_data = {k: parsed_metrics[k] for k in keys if k in parsed_metrics}
                        if equip_data:
                            client.publish(
                                f"ocp/grinding/equipment/{equip_id}",
                                json.dumps({
                                    "equipment_id": equip_id,
                                    "record_no": record_no,
                                    "time": time_str,
                                    "elapsed_hrs": elapsed_hrs,
                                    "metrics": equip_data
                                })
                            )

                    print(f"[replay-service] Replayed Record #{record_no} (Time: {time_str}) -> MQTT: {TOPIC_TELEMETRY}", flush=True)
                    time.sleep(REPLAY_INTERVAL)

                print(f"[replay-service] Completed full replay of {row_count} SysCAD readings. Restarting replay loop...", flush=True)
        except Exception as e:
            print(f"[replay-service] Error reading CSV file: {e}. Retrying in 5 seconds...", flush=True)
            time.sleep(5)

if __name__ == "__main__":
    main()
