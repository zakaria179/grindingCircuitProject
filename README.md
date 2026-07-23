# OCP Ore Grinding Circuit Digital Twin 🏭⚡

A professional-grade, open-source industrial **Digital Twin of OCP's Phosphate Ore Grinding Circuit**, modeled around a closed-loop flowsheet:
`Slurry_In` ➔ **Pump Box (`PB_001`)** ➔ **Slurry Pump (`SP_001`)** ➔ **Hydrocyclones (`CY_001`)** ➔ **Ball Mill (`BM_001`)** ➔ `Slurry_Out` (to flotation), with coarse hydrocyclone underflow recycling back to `PB_001`.

Built with a $0 software budget using industry-standard open-source tools (Docker Compose, Eclipse Mosquitto, Node-RED, Ignition Maker Edition, Neo4j Community, MinIO, Blender, three.js, React), this project provides real-time SCADA telemetry monitoring, data contextualization, Industry 4.0 Asset Administration Shell (AAS) knowledge graphs, and interactive 2D/3D visualization.

> ⚠️ **IMPORTANT**: Always check [PROJECT_STATUS.md](file:///home/zakaria/Documents/grindingCircuitProject/PROJECT_STATUS.md) for the active build state before creating or modifying code.

---

## 📐 Process Flowsheet & Circuit Topology

```
                       ┌──────────────────────────────────────────────┐
                       │                                              │
                       ▼                                              │
  [Slurry_In] ──► [PB_001 Pump Box] ──► [SP_001 Slurry Pump] ──► [CY_001 Hydrocyclone]
  (Fresh Feed)    (Recovers Recycle)    (Discharge to Cyclones)    (160 µm Target Cut)
                                                                      │          │
                                                Underflow (>160 µm)  │          │ Overflow (≤160 µm)
                                                ┌─────────────────────┘          ▼
                                                ▼                          [Slurry_Out]
                                       [BM_001 Ball Mill]              (Flotation Feed)
                                       (Ground to 160 µm P80)
                                                │
                                                └──────────────────────────────► [PB_001]
```

* **Target Output Particle Size**: 80% passing **160 µm** ($P_{80} = 160\,\mu\text{m}$).
* **Recirculating Load**: Coarse material exceeding $160\,\mu\text{m}$ is separated at hydrocyclone `CY_001` underflow and returned to `PB_001` for re-grinding in `BM_001`.

---

## 🏗️ System Architecture & Services Stack

```
 ┌──────────────────┐
 │  replay-service  │ (Python CSV Replayer)
 └────────┬─────────┘
          │ (Raw MQTT Telemetry)
          ▼
 ┌──────────────────┐     (Port 1883)
 │    Mosquitto     │ ◄──────────────────────────────┐
 └────────┬─────────┘                                │
          │                                          │
          ▼                                          │
 ┌──────────────────┐ (Port 1880)                    │
 │     Node-RED     │ ── (Enriched KPI Topics) ──────┘
 └────────┬─────────┘
          │
          ├─────────────────────────┬────────────────────────┐
          ▼                         ▼                        ▼
 ┌──────────────────┐      ┌──────────────────┐     ┌──────────────────┐
 │ Ignition SCADA   │      │  Neo4j Graph DB  │     │   MinIO Object   │
 │ (2D Synoptic)    │      │  (AAS Knowledge) │     │     Storage      │
 └──────────────────┘      └──────────────────┘     └──────────────────┘
    (Port 8088)               (Port 7474)              (Port 9091)
```

---

## 🗺️ Phase Roadmap & Comprehensive Details

### - [x] **Phase 00 — Foundation & Microservices Infrastructure**
* **Status**: Completed (`[x]`)
* **Details**: Established containerized microservice foundation via `docker-compose.yml`. Configured default networking, persistent data volumes (`neo4j_data`, `minio_data`, `ignition_data`, `nodered_data`), and default environment variables. Includes empirical health checks for all service ports.

### - [x] **Phase 01 — Pipeline Connection Testing (SysCAD CSV Replay ➔ MQTT)**
* **Status**: Completed (`[x]`)
* **Details**: Built the `replay-service` microservice parsing a 482-record SysCAD continuous simulation dataset (`data.csv`). Streams telemetry every second over Mosquitto MQTT broker on `ocp/grinding/telemetry` and targeted equipment topics (`ocp/grinding/equipment/{equip_id}`).

### - [x] **Phase 02 — 2D SCADA Visualization & Node-RED Data Contextualization**
* **Status**: Completed (`[x]`)
* **Details**: Integrated **Node-RED** (Port `1880`) for telemetry enrichment, computing recirculating load ratios, target $P_{80}$ deviations, and alarm thresholds. Integrated **Ignition Maker Edition** (Port `8088`) with complete SCADA Tag Provider exports ([viz-2d/tags.json](file:///home/zakaria/Documents/grindingCircuitProject/viz-2d/tags.json)) and Perspective 2D Synoptic View ([viz-2d/flowsheet_perspective_view.json](file:///home/zakaria/Documents/grindingCircuitProject/viz-2d/flowsheet_perspective_view.json)).

### - [ ] **Phase 03 — 3D Industrial Visualization (Blender + three.js)**
* **Status**: Planned (`[ ]`)
* **Details**: Building GLTF low-poly 3D models for equipment and piping in Blender. Rendering an interactive 3D WebGL scene via three.js with real-time speed animations (ball mill rotation rate, slurry flow particle speed) bound to live MQTT flow parameters.

### - [ ] **Phase 04 — Knowledge Graph & Asset Administration Shell (AAS)**
* **Status**: Planned (`[ ]`)
* **Details**: Creating Industry 4.0 Asset Administration Shell (AAS) submodels (Nameplate, Operational Data, Technical Manuals) using IDTA standards. Modeling equipment relationships in Neo4j Community Edition using Cypher graph queries and Protégé OWL ontologies.

### - [ ] **Phase 05 — Unified React Monitoring Dashboard**
* **Status**: Planned (`[ ]`)
* **Details**: Developing a modern single-pane-of-glass React + Vite web dashboard embedding Ignition 2D views, three.js 3D canvas, live KPI cards, and equipment slide-out detail drawers.

### - [ ] **Phase 06 — Predictive Maintenance & Flow Optimization**
* **Status**: Parked (`[ ]`)
* **Details**: Parked until realistic sensor failure datasets are available.

---

## 🛠️ Operations & Getting Started

### Prerequisites
* **Linux / Ubuntu**: Docker Engine + Docker Compose (v2+)
* **Windows**: Docker Desktop (See [ZINEB_GUIDE.md](file:///home/zakaria/Documents/grindingCircuitProject/ZINEB_GUIDE.md) for full step-by-step setup)

### Quick Commands

#### Start all microservices
```bash
docker compose up -d
```

#### Inspect running containers
```bash
docker compose ps
```

#### View service logs
```bash
docker compose logs -f replay-service
```

#### Stop all services
```bash
docker compose down
```

---

## 🌐 Service Access URLs

| Service | Port / Access URL | Purpose | Default Credentials |
| :--- | :--- | :--- | :--- |
| **Node-RED** | [http://localhost:1880](http://localhost:1880) | Data Integration & Contextualization Engine | *None* |
| **Ignition SCADA Gateway** | [http://localhost:8088](http://localhost:8088) | 2D HMI & Perspective Views | `admin` / `changeme123` |
| **Neo4j Graph Browser** | [http://localhost:7474](http://localhost:7474) | AAS Knowledge Graph Database | `neo4j` / `changeme123` |
| **MinIO Console** | [http://localhost:9091](http://localhost:9091) | Object Storage for Models & Data | `minioadmin` / `minioadmin` |
| **Mosquitto Broker** | `localhost:1883` (MQTT) / `localhost:9001` (WS) | Messaging Infrastructure | *None* |
