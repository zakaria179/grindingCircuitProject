# Phase 00 — Foundation & Team Setup

* **Status**: Completed (`[x]`)
* **Master Plan Section**: Section 02 (`#phase0`) in [`digital_twin_grinding_circuit_plan (1).html`](file:///home/zakaria/Documents/grindingCircuitProject/digital_twin_grinding_circuit_plan%20%281%29.html)

---

## 📌 Context & Objective

Phase 00 exists specifically to fix what went wrong during previous unorganized Docker attempts. Operating across two different operating systems (Ubuntu Linux and Windows Docker Desktop) with two team members requires a single, reproducible execution command and strict folder structure.

---

## 🏗️ Folder Structure & Repository Organization

The repository is structured into isolated, service-aligned directories:

```
/grindingCircuitProject
├── broker/                  # Mosquitto MQTT configuration (mosquitto.conf)
├── replay-service/          # CSV Telemetry Replay microservice & SysCAD data
├── viz-2d/                  # Ignition Maker Edition 2D SCADA views & tag exports
├── viz-3d/                  # Blender 3D GLTF models & three.js WebGL viewer
├── graph/                   # Protégé OWL ontology & Neo4j Cypher scripts
├── dashboard/               # React + Vite monitoring dashboard UI
├── ai-ml/                   # Predictive maintenance & optimization (parked)
├── docs/                    # Phase documentation library
├── docker-compose.yml       # Master container orchestrator
├── README.md                # Quick start & architecture overview
├── ZINEB_GUIDE.md           # Step-by-step Windows Docker Desktop runner guide
└── PROJECT_STATUS.md        # Single source of truth for phase progress
```

---

## 🛠️ Microservice Architecture & `docker-compose.yml`

Docker Compose orchestrates the $0 open-source infrastructure:

### 1. `mosquitto` (MQTT Broker)
- **Image**: `eclipse-mosquitto:latest`
- **Ports**: `1883` (TCP MQTT) / `9001` (WebSockets)
- **Config**: `/broker/mosquitto.conf` (allows anonymous connections for dev)

### 2. `neo4j` (Knowledge Graph)
- **Image**: `neo4j:community`
- **Ports**: `7474` (HTTP Browser) / `7687` (Bolt Driver)
- **Environment**: `NEO4J_AUTH=neo4j/changeme123`
- **Volume**: `neo4j_data`

### 3. `minio` (Object Storage)
- **Image**: `minio/minio:latest`
- **Ports**: `9000` (API) / `9091` (Web Console)
- **Environment**: `MINIO_ROOT_USER=minioadmin`, `MINIO_ROOT_PASSWORD=minioadmin`
- **Volume**: `minio_data`

### 4. `replay-service` (CSV Streamer)
- **Build**: `./replay-service`
- **Role**: Reads `Dynamic_Results.csv` (`data.csv`) and publishes MQTT streams to Mosquitto.

### 5. `ignition` (2D HMI)
- **Image**: `kcollins/ignition:8.1.33`
- **Ports**: `8088` (HTTP Gateway) / `8043` (HTTPS)
- **License**: Ignition Maker Edition (free non-commercial license)
- **Volume**: `ignition_data`

### 6. `node-red` (Edge & Contextualization)
- **Image**: `nodered/node-red:latest`
- **Port**: `1880`
- **Volume**: `nodered_data`

---

## 📋 Verification & Deliverables

1. **One-Command Environment Launch**:
   ```bash
   docker compose up -d
   ```
2. **Container Status Check**:
   ```bash
   docker compose ps
   ```
3. **Cross-Platform Verification**:
   - Tested and verified on **Ubuntu Linux** natively.
   - Tested and verified on **Windows** using Docker Desktop (WSL 2 backend) via [ZINEB_GUIDE.md](file:///home/zakaria/Documents/grindingCircuitProject/ZINEB_GUIDE.md).
