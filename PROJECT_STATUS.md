# Digital Twin Master Plan — Project Status & Roadmap

Single source of truth tracking project build status against the master plan specification in [digital_twin_grinding_circuit_plan (1).html](file:///home/zakaria/Documents/grindingCircuitProject/digital_twin_grinding_circuit_plan%20%281%29.html).

---

## 📌 Phase Roadmap & Build Status

### - [x] **Phase 00 — Foundation & Team Setup**
* **Status**: Completed (`[x]`)
* **Plan Ref**: Section 02 (`#phase0`) in HTML plan.
* **Detailed Documentation**: [`docs/PHASE_00_FOUNDATION_TEAM_SETUP.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_00_FOUNDATION_TEAM_SETUP.md)
* **Scope & Artifacts**: Shared git repository layout, `docker-compose.yml` orchestrating `mosquitto`, `neo4j`, `minio`, `replay-service`, `ignition`, `node-red`, verified cross-platform on Ubuntu Linux and Windows (Docker Desktop).

---

### - [x] **Phase 01 — Simulated Live Feed**
* **Status**: Completed (`[x]`)
* **Plan Ref**: Section 03 (`#phase1`) in HTML plan.
* **Detailed Documentation**: [`docs/PHASE_01_SIMULATED_LIVE_FEED.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_01_SIMULATED_LIVE_FEED.md)
* **Scope & Artifacts**: CSV replay microservice parsing SysCAD `Dynamic_Results.csv` (`data.csv`) publishing telemetry row-by-row to Mosquitto MQTT broker on `circuit/*` topics, with static granulometric benchmark overlay (%BPL / Cd).

---

### - [x] **Phase 02 — 2D Visualization**
* **Status**: Completed (`[x]`)
* **Plan Ref**: Section 04 (`#phase2`) in HTML plan.
* **Detailed Documentation**: [`docs/PHASE_02_2D_VISUALIZATION.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_02_2D_VISUALIZATION.md)
* **Scope & Artifacts**: Ignition Maker Edition Gateway commission, Perspective module 2D flowsheet synoptic view (`PB_001` → `SP_001` → `BM_001` → `CY_001`), MQTT Engine tag bindings, pipe percent solids coloring, flow animations, 160 µm cut point target band, and Node-RED KPI calculations.

---

### - [ ] **Phase 03 — 3D Visualization**
* **Status**: Planned (`[ ]`)
* **Plan Ref**: Section 05 (`#phase3`) in HTML plan.
* **Detailed Documentation**: [`docs/PHASE_03_3D_VISUALIZATION.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_03_3D_VISUALIZATION.md)
* **Scope & Artifacts**: Blender low-poly geometry modeling for Pump Box (`PB_001`), Slurry Pump (`SP_001`), Ball Mill (`BM_001`), and Cyclone Cluster (`CY_001`). GLTF scene loading in three.js WebGL canvas animated via MQTT stream (mill rotation, slurry tint, particle flow).

---

### - [ ] **Phase 04 — Knowledge Graph & Asset Administration Shell (AAS)**
* **Status**: Planned (`[ ]`)
* **Plan Ref**: Section 06 (`#phase4`) in HTML plan.
* **Detailed Documentation**: [`docs/PHASE_04_KNOWLEDGE_GRAPH_AAS.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_04_KNOWLEDGE_GRAPH_AAS.md)
* **Scope & Artifacts**: Protégé OWL ontology (`Pump`, `PumpBox`, `Mill`, `CycloneCluster`, `Stream`; relationships `feeds`, `discharges_to`, `recycles_to`), Neo4j Community graph instance, Eclipse BaSyx AAS server with 4 equipment submodels, Cypher circulating load query.

---

### - [ ] **Phase 05 — Dashboard & KPIs**
* **Status**: Planned (`[ ]`)
* **Plan Ref**: Section 07 (`#phase5`) in HTML plan.
* **Detailed Documentation**: [`docs/PHASE_05_DASHBOARD_KPIS.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_05_DASHBOARD_KPIS.md)
* **Scope & Artifacts**: Single-pane React application embedding Ignition 2D Perspective iframe and three.js 3D WebGL scene, Recharts live trend charts, granulometric benchmark panel (%BPL/Cd), circulating-load Cypher tile, and 160 µm cut deviation alerts.

---

### - [ ] **Phase 06 — Predictive Maintenance & Flow Optimization**
* **Status**: Parked (`[ ]` — PARKED)
* **Plan Ref**: Section 08 (`#phase6`) in HTML plan.
* **Detailed Documentation**: [`docs/PHASE_06_PREDICTIVE_MAINTENANCE_PARKED.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_06_PREDICTIVE_MAINTENANCE_PARKED.md)
* **Scope & Artifacts**: Explicitly parked until Phases 00–05 are running cleanly on validated empirical data to prevent GIGO model training.
