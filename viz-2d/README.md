# Phase 02 — 2D SCADA Visualization & Data Contextualization

This directory contains the industrial 2D SCADA / HMI configuration assets and tag definitions for OCP's Phosphate Ore Grinding Circuit, implemented using **Ignition Maker Edition** alongside **Node-RED** for data integration.

---

## 📌 Architecture & System Role

Phase 02 converts raw MQTT telemetry streams from `replay-service` into real-time industrial SCADA tags and interactive synoptic views:

```
[SysCAD Replay / Sensors] 
       │
       ▼ (Raw MQTT: ocp/grinding/telemetry)
[Mosquitto Broker]
       │
       ▼
[Node-RED Data Engine] (Port 1880)
       │  • Computes recirculating load & P80 target deviations (160 µm)
       │  • Contextualizes equipment health & operational status
       ▼ (Enriched MQTT: ocp/grinding/contextualized/...)
[Ignition SCADA Gateway] (Port 8088)
       │  • Imports SCADA Tag Provider (`tags.json`)
       │  • Displays Perspective 2D Synoptic View (`flowsheet_perspective_view.json`)
```

---

## 🛠️ Files & Assets Included

* **`tags.json`**: Ignition Tag Provider export defining structured memory and expression tags mapped to MQTT Engine topics for all circuit equipment (`Slurry_In`, `PB_001`, `SP_001`, `CY_001`, `BM_001`, `Slurry_Out`).
* **`flowsheet_perspective_view.json`**: Complete Ignition Perspective 2D Synoptic View schema representing the closed-loop flowsheet:
  - `Slurry_In` ➔ `PB_001` (Pump Box) ➔ `SP_001` (Slurry Pump) ➔ `CY_001` (Hydrocyclones, 160 µm cut) ➔ `BM_001` (Ball Mill, 160 µm target) ➔ `Slurry_Out` (Flotation feed), with `CY_001` coarse underflow recycling back to `PB_001`.

---

## 🚀 Operations & Ignition Import Instructions

### 1. Launching via Docker Compose
Ignition and Node-RED run as core services in `docker-compose.yml`:
```bash
docker compose up -d
```

* **Node-RED UI**: [http://localhost:1880](http://localhost:1880)
* **Ignition SCADA Gateway**: [http://localhost:8088](http://localhost:8088) (Credentials: `admin` / `changeme123`)

### 2. Importing Assets into Ignition Designer
1. Open the **Ignition Gateway Web Interface** at `http://localhost:8088`.
2. Ensure the **MQTT Engine** module (Cirrus Link) is active and connected to `tcp://mosquitto:1883`.
3. Launch **Ignition Designer** and open the Tag Browser.
4. Import `tags.json` into the `default` Tag Provider.
5. Import `flowsheet_perspective_view.json` under **Perspective > Views** to view the live animated grinding circuit flowsheet.
