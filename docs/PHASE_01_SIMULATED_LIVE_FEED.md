# Phase 01 — Simulated Live Feed

* **Status**: Completed (`[x]`)
* **Master Plan Section**: Section 03 (`#phase1`) in [`digital_twin_grinding_circuit_plan (1).html`](file:///home/zakaria/Documents/grindingCircuitProject/digital_twin_grinding_circuit_plan%20%281%29.html)

---

## 📌 Context & Objective

Since direct PLC/SCADA access to OCP's physical grinding line is unavailable, SysCAD dynamic simulation output (`Dynamic_Results.csv` stored as `/replay-service/data.csv`) serves as ground truth. Phase 01 turns this CSV file into a live stream that behaves identically to an OPC-UA / MQTT tag engine.

---

## ⚙️ Service Architecture (`/replay-service`)

The replay service is written in Python 3 using `paho-mqtt` (v2 API):

```
┌─────────────────────────────────────────────────────────────┐
│                      replay-service                         │
│                                                             │
│  ┌───────────────────────┐                                  │
│  │ Dynamic_Results.csv   │ ── (Pandas / DictReader) ──┐    │
│  └───────────────────────┘                            │     │
│  ┌───────────────────────┐                            ▼     │
│  │ Granulometric Benchmark│ ── (Published at Startup) ──► Paho│
│  │ %BPL / Cd Curve       │                              MQTT│
│  └───────────────────────┘                            │     │
└───────────────────────────────────────────────────────┼─────┘
                                                        │ MQTT Stream
                                                        ▼
                                            ┌───────────────────────┐
                                            │   Mosquitto Broker    │
                                            │     TCP :1883         │
                                            └───────────────────────┘
```

---

## 🏷️ Topic Taxonomy & Tag Dictionary

Topic naming strictly mirrors the flowsheet equipment tags:

### 1. Equipment Level Topics
- `circuit/PB_001/level_percent`: Pump Box level (%)
- `circuit/SP_001/flow_m3h`: Slurry Pump discharge rate ($m^3/h$)
- `circuit/BM_001/discharge/percent_bpl`: Ball Mill discharge %BPL grade
- `circuit/BM_001/power_kw`: Ball Mill power draw ($kW$)
- `circuit/CY_001/underflow/p80`: Cyclone underflow particle size ($\mu m$)
- `circuit/CY_001/overflow/p80`: Cyclone overflow particle size (target $160\,\mu m$)

### 2. Static Reference Overlay
- `circuit/granulometric_benchmark`: Published once at startup containing %BPL grade and Cadmium (Cd) contaminant curve parameters.

### 3. Loop & Speed Control
- Supports a configurable replay speed multiplier (`REPLAY_SPEED_MULTIPLIER=1.0` for 1.0s demo steps vs real-time ~16 min/step execution) and an infinite loop flag (`REPLAY_LOOP=true`).

---

## 📋 Verification & Deliverables

1. **Replay Service Code**: `/replay-service/main.py`
2. **Dataset File**: `/replay-service/data.csv` (482 dynamic records)
3. **Verification Command**:
   ```bash
   docker compose exec mosquitto mosquitto_sub -t "circuit/#" -v
   ```
   *Output*: Live telemetry payloads streaming continuously.
