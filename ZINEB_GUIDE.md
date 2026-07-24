# Zineb's Windows Setup & Execution Guide 🚀

Hi Zineb! This guide is aligned with our master plan file: [digital_twin_grinding_circuit_plan.html](file:///home/zakaria/Documents/grindingCircuitProject/digital_twin_grinding_circuit_plan.html).

---

## 📌 Current Project Status & Architecture

- **Active Microservices**:
  1. `mosquitto`: MQTT messaging broker (`:1883` TCP, `:9001` WebSockets)
  2. `replay-service`: Telemetry replayer streaming SysCAD data (`Dynamic_Results.csv` / `data.csv`)
  3. `node-red`: Data integration & contextualization engine (`:1880`)
  4. `ignition`: Industrial 2D SCADA HMI gateway (`:8088`)
  5. `neo4j`: AAS Knowledge Graph database (`:7474`)
  6. `minio`: Object storage console (`:9091`)

---

## 🌐 Quick Access Links & Web Interfaces

| Service | Web Access URL | Credentials | Purpose |
| :--- | :--- | :--- | :--- |
| **Node-RED** | [http://localhost:1880](http://localhost:1880) | *No Login Required* | Build data flows & contextualize telemetry |
| **Ignition SCADA Gateway** | [http://localhost:8088](http://localhost:8088) | User: `admin`<br>Password: `changeme123` | 2D SCADA Perspective Views & Tag Engine |
| **Neo4j Graph Browser** | [http://localhost:7474](http://localhost:7474) | User: `neo4j`<br>Password: `changeme123` | Inspect Asset Knowledge Graph |
| **MinIO Console** | [http://localhost:9091](http://localhost:9091) | User: `minioadmin`<br>Password: `minioadmin` | Access stored models & CSV artifacts |
| **Mosquitto MQTT** | `localhost:1883` | *No Web UI* | MQTT Messaging Spine |

---

## 🛠️ Step-by-Step Instructions for Windows

### Step 1: Prepare Docker Desktop
1. Ensure **Docker Desktop for Windows** is installed and running (look for the whale icon in your taskbar).
2. Ensure WSL 2 backend is enabled.

### Step 2: Open Terminal / VS Code & Pull Latest Changes
```powershell
git pull origin main
```

### Step 3: Launch All Microservices
```powershell
docker compose up -d
```

### Step 4: Verify Container Status
```powershell
docker compose ps
```

### Step 5: Explore Phase Documentation
All detailed phase specifications are available in the [`docs/`](file:///home/zakaria/Documents/grindingCircuitProject/docs/README.md) directory:
- [Phase 00: Foundation & Setup](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_00_FOUNDATION_TEAM_SETUP.md)
- [Phase 01: Simulated Live Feed](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_01_SIMULATED_LIVE_FEED.md)
- [Phase 02: 2D Visualization](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_02_2D_VISUALIZATION.md)
- [Phase 03: 3D Visualization](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_03_3D_VISUALIZATION.md)
- [Phase 04: Knowledge Graph & AAS](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_04_KNOWLEDGE_GRAPH_AAS.md)
- [Phase 05: Dashboard & KPIs](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_05_DASHBOARD_KPIS.md)
- [Phase 06: Predictive Maintenance](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_06_PREDICTIVE_MAINTENANCE_PARKED.md)
