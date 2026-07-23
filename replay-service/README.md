# Replay Service — SysCAD CSV Telemetry Publisher

The `replay-service` is a Python-based microservice that simulates real-time IoT sensor telemetry from OCP's phosphate ore grinding circuit by reading historical SysCAD simulation data and streaming it to the Mosquitto MQTT broker.

---

## 📌 Features & Responsibilities

1. **Dataset Replay**: Parses `data.csv` (482 continuous industrial readings from SysCAD).
2. **Master Telemetry Stream**: Publishes raw dataset records to `ocp/grinding/telemetry`.
3. **Targeted Equipment Telemetry**: Segregates metrics per physical asset and publishes to targeted MQTT topics (`ocp/grinding/equipment/{equip_id}`).
4. **Resilient Connection Handling**: Auto-reconnects to Mosquitto with exponential backoff if the broker restarts.

---

## 🛠️ Data Fields & Mappings

The SysCAD dataset tracks key physical metrics across the grinding loop:

| Metric Name | Unit | Target Equipment | Description |
| :--- | :--- | :--- | :--- |
| `Feed Solid Flow` | t/h | `Slurry_In`, `PB_001` | Fresh ore solid mass flow rate |
| `Feed BPL` | % | `Slurry_In` | Bone Phosphate of Lime (phosphate grade %) |
| `Feed P80` | µm | `Slurry_In` | Particle size 80% passing diameter of fresh feed |
| `Feed Solid Fraction` | % | `Slurry_In` | Solid mass percentage in slurry |
| `Cyclone Feed Solid Flow` | t/h | `SP_001`, `CY_001` | Slurry pump discharge to hydrocyclones |
| `Cyclone Underflow Solid Flow` | t/h | `CY_001`, `PB_001` | Coarse fraction (>160 µm) recycled to pump box |
| `Cyclone Underflow P80` | µm | `CY_001` | Particle size of recycled coarse stream |
| `Ball Mill Discharge Solid Flow` | t/h | `BM_001` | Output flow from ball mill |
| `Ball Mill Discharge P80` | µm | `BM_001` | Ground particle size (Target: 160 µm) |
| `Output Slurry Solid Flow` | t/h | `Slurry_Out` | Final overflow sent to flotation |
| `Output Slurry P80` | µm | `Slurry_Out` | Final product particle size (Target cut: 160 µm) |

---

## 🛰️ Published MQTT Topics

* **Master Stream**: `ocp/grinding/telemetry`
* **Equipment Specific**:
  - `ocp/grinding/equipment/Slurry_In`
  - `ocp/grinding/equipment/PB_001`
  - `ocp/grinding/equipment/SP_001`
  - `ocp/grinding/equipment/CY_001`
  - `ocp/grinding/equipment/BM_001`
  - `ocp/grinding/equipment/Slurry_Out`

---

## ⚙️ Environment Variables

* `MQTT_BROKER`: Broker hostname (Default: `mosquitto`)
* `MQTT_PORT`: Broker port (Default: `1883`)
* `REPLAY_INTERVAL`: Delay in seconds between replaying CSV rows (Default: `1.0` second)
