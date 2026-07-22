# Phase 02 — 2D Visualization (Ignition Maker Edition)

This directory contains the SCADA / HMI configuration assets for OCP's Phosphate Ore Grinding Circuit using **Ignition Maker Edition** (free, non-commercial license).

---

## 📌 Files Included

- **`tags.json`**: Ignition Tag Provider export defining all SCADA tags mapped to Mosquitto MQTT topics (`ocp/grinding/...`).
- **`flowsheet_perspective_view.json`**: Ignition Perspective 2D Synoptic View JSON representing the closed-loop flowsheet:
  `Slurry_In` -> `PB_001` -> `SP_001` -> `CY_001` (160µm cut) -> `BM_001` (160µm target) -> `Slurry_Out`, with `CY_001` underflow recycling back to `PB_001`.

---

## 🚀 How to Run & Import into Ignition

### Option 1: Via Docker Compose (Included)
Ignition is configured as a service in `docker-compose.yml`:

```bash
docker compose up -d ignition
```

Access the Ignition Gateway at: [http://localhost:8088](http://localhost:8088)  
- **Username**: `admin`
- **Password**: `changeme123`

### Option 2: Connecting MQTT Engine to Mosquitto
1. Open the Ignition Gateway Web Interface at `http://localhost:8088`.
2. Install / enable the **MQTT Engine** module (Cirrus Link).
3. Set the MQTT Server URI to: `tcp://mosquitto:1883` (or `tcp://localhost:1883` if running outside Docker).
4. Import `tags.json` in the Ignition Designer Tag Browser.
5. Import `flowsheet_perspective_view.json` under **Perspective > Views** in Ignition Designer.
