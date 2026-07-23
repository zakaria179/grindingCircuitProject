# Grinding Circuit Project — Status & Detailed Phase Roadmap

This file is the single source of truth for the project build status. Always check this file before creating or modifying code, and update it upon completing work.

---

## 📌 Detailed Phase Roadmap & Build Status

### - [x] **Phase 00 — Foundation & Microservices Setup**
* **Status**: Completed (`[x]`)
* **Core Artifacts & Infrastructure**:
  - `docker-compose.yml`: Microservice orchestrator managing 6 core services (`mosquitto`, `neo4j`, `minio`, `replay-service`, `ignition`, `nodered`).
  - Persistent Volumes: Configured `neo4j_data`, `minio_data`, `ignition_data`, and `nodered_data`.
  - Service Configuration: `/broker/mosquitto.conf` (MQTT port `1883`, WebSockets port `9001`).
  - Documentation: Master [README.md](file:///home/zakaria/Documents/grindingCircuitProject/README.md), team guide [ZINEB_GUIDE.md](file:///home/zakaria/Documents/grindingCircuitProject/ZINEB_GUIDE.md), and phase status tracking in [PROJECT_STATUS.md](file:///home/zakaria/Documents/grindingCircuitProject/PROJECT_STATUS.md).
* **Empirical Verification**: All 6 containers confirmed running via `docker compose ps` and responding cleanly on assigned ports.

---

### - [x] **Phase 01 — Telemetry Pipeline (SysCAD CSV Replay ➔ MQTT)**
* **Status**: Completed (`[x]`)
* **Core Artifacts & Infrastructure**:
  - `/replay-service/main.py`: Python MQTT client using Paho MQTT `v2` protocol.
  - `/replay-service/data.csv`: 482 continuous industrial simulation records from SysCAD.
  - MQTT Topics: Streaming raw records to `ocp/grinding/telemetry` and equipment-specific streams (`ocp/grinding/equipment/{equip_id}`).
* **Empirical Verification**: Container logs verified streaming CSV records continuously every 1.0s.

---

### - [x] **Phase 02 — 2D SCADA Visualization & Node-RED Contextualization**
* **Status**: Completed (`[x]`)
* **Core Artifacts & Infrastructure**:
  - **Node-RED Engine**: Service container running on port `1880` (`nodered/node-red:latest`) for telemetry enrichment, calculating recirculating load ratios, target $P_{80}$ deviations (160 µm cut point), and alarm threshold evaluations.
  - **Ignition SCADA Gateway**: Running on port `8088` (`kcollins/ignition:8.1.33`).
  - [viz-2d/tags.json](file:///home/zakaria/Documents/grindingCircuitProject/viz-2d/tags.json): Ignition Tag Provider export mapping SCADA expression and memory tags to MQTT topics.
  - [viz-2d/flowsheet_perspective_view.json](file:///home/zakaria/Documents/grindingCircuitProject/viz-2d/flowsheet_perspective_view.json): Ignition Perspective 2D Synoptic View representing the closed-loop flowsheet (`Slurry_In` ➔ `PB_001` ➔ `SP_001` ➔ `CY_001` ➔ `BM_001` ➔ `Slurry_Out` with underflow recycle).
* **Empirical Verification**: Ignition Gateway and Node-RED active and responding cleanly on ports `:8088` and `:1880`.

---

### - [ ] **Phase 03 — 3D Industrial Visualization (Blender + three.js)**
* **Status**: Not Started (`[ ]`)
* **Directory**: `/viz-3d`
* **Target Scope**: Low-poly GLTF equipment modeling in Blender, interactive 3D WebGL scene rendering via three.js, real-time animation of ball mill rotation and slurry flow particles bound to MQTT flow rates.

---

### - [ ] **Phase 04 — Knowledge Graph & Asset Administration Shell (AAS)**
* **Status**: Not Started (`[ ]`)
* **Directory**: `/graph`
* **Target Scope**: Industry 4.0 Asset Administration Shell (AAS) submodel definitions (IDTA standard), Neo4j Community property graph model for equipment topology, Cypher queries for lineage and fault propagation tracing.

---

### - [ ] **Phase 05 — Unified React Monitoring Dashboard**
* **Status**: Not Started (`[ ]`)
* **Directory**: `/dashboard`
* **Target Scope**: Modern React + Vite web dashboard embedding Ignition SCADA 2D views, three.js 3D canvas, live KPI cards, equipment slide-out detail drawers, and historical trend charts.

---

### - [ ] **Phase 06 — Predictive Maintenance & Flow Optimization**
* **Status**: Parked (`[ ]` — PARKED)
* **Directory**: `/ai-ml`
* **Target Scope**: Parked until realistic sensor failure data is available. Do not write code here.
