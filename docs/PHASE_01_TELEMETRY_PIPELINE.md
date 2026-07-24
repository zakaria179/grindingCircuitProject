# Phase 01 — Telemetry Pipeline (SysCAD CSV Replay ➔ MQTT)

## 📌 Executive Summary & Status
* **Status**: `[x] COMPLETED`
* **Target Objective**: Build an automated telemetry ingestion microservice that reads dynamic industrial simulation outputs from SysCAD (`data.csv`) and publishes structured JSON telemetry payloads over Eclipse Mosquitto MQTT broker at a continuous 1.0s interval.

---

## 🏭 Industrial Dataset & Telemetry Source

The ground-truth simulation data originates from a continuous process run of OCP's phosphate grinding line, stored in `/replay-service/data.csv`:
- **Record Count**: 482 continuous time-series records.
- **Sample Metrics**:
  - `slurry_flow_m3h`: Volumetric slurry flow rate ($m^3/h$)
  - `solid_tph`: Dry solids mass flow rate ($t/h$)
  - `percent_solids`: Slurry percent solids concentration (%)
  - `percent_bpl`: Phosphate grade metric (% Bone Phosphate of Lime)
  - `cadmium_ppm`: Contaminant metric (Cd concentration in ppm)
  - `p80_microns`: Particle size 80% passing specification ($\mu m$)
  - `mill_power_kw`: Ball mill power draw ($kW$)
  - `cyclone_pressure_kpa`: Hydrocyclone operating feed pressure ($kPa$)

---

## 🏗️ Replay Service Architecture (`/replay-service`)

The microservice is implemented in Python 3.11 using the modern **Paho MQTT v2 Client API** (`paho-mqtt>=2.0.0`).

```
┌─────────────────────────────────────────────────────────────┐
│                      replay-service                         │
│                                                             │
│  ┌──────────────┐     Pandas / CSV     ┌─────────────────┐  │
│  │   data.csv   │ ───────────────────► │ Python Publisher│  │
│  └──────────────┘                      └────────┬────────┘  │
└─────────────────────────────────────────────────┼───────────┘
                                                  │ MQTT JSON
                                                  ▼
                                      ┌───────────────────────┐
                                      │   Mosquitto Broker    │
                                      │     TCP :1883         │
                                      └───────────────────────┘
```

### 1. Topic Taxonomy & Payload Structure

The replay service broadcasts telemetry across two distinct hierarchical topic structures:

#### A. Central Telemetry Stream (`ocp/grinding/telemetry`)
Aggregated JSON snapshot containing state records for all 4 circuit components plus feed/discharge streams:
```json
{
  "timestamp": 1721810400,
  "record_index": 42,
  "circuit": {
    "target_p80_microns": 160.0,
    "feed_flow_m3h": 450.2,
    "product_p80_microns": 158.4
  },
  "equipment": {
    "PB_001": { "level_percent": 68.5, "slurry_flow_m3h": 720.0, "percent_solids": 55.2 },
    "SP_001": { "flow_m3h": 720.0, "pressure_kpa": 145.0, "power_kw": 185.0 },
    "CY_001": { "feed_pressure_kpa": 145.0, "overflow_p80": 158.4, "underflow_p80": 245.0, "split_ratio": 0.65 },
    "BM_001": { "power_kw": 1450.0, "pulp_density": 72.0, "sound_db": 94.2 }
  }
}
```

#### B. Granular Equipment Topics (`ocp/grinding/equipment/{equip_id}`)
- `ocp/grinding/equipment/PB_001` (Pump Box)
- `ocp/grinding/equipment/SP_001` (Slurry Pump)
- `ocp/grinding/equipment/CY_001` (Hydrocyclone Cluster)
- `ocp/grinding/equipment/BM_001` (Ball Mill)

---

## 🛠️ Implementation Details

### `replay-service/main.py` Key Features
- **Paho MQTT v2 Callback API**: Handles `on_connect`, `on_publish`, and automatic reconnection backoff without blocking main execution threads.
- **Continuous Loop**: Automatically wraps back to record index 0 upon reaching row 482 for uninterrupted long-running SCADA testing.
- **Graceful Signal Handling**: Listens for SIGTERM/SIGINT to safely disconnect MQTT client sockets upon container teardown.

---

## 📋 Verification & Testing Commands

### 1. Inspect Service Logs
```bash
docker compose logs -f replay-service
```
*Expected Output*: `[INFO] Published row 42/482 to ocp/grinding/telemetry`.

### 2. Live MQTT Subscription (via CLI)
Using Mosquitto CLI inside the container or host:
```bash
docker compose exec mosquitto mosquitto_sub -t "ocp/grinding/#" -v
```
*Expected Output*: Live JSON streams received every 1.0 second.

---

## 📂 Repository Artifacts
- `/replay-service/main.py`: Main telemetry publisher logic.
- `/replay-service/data.csv`: SysCAD dynamic process simulation dataset.
- `/replay-service/Dockerfile`: Python container build specification.
- `/replay-service/requirements.txt`: Dependencies (`paho-mqtt>=2.0.0`).
