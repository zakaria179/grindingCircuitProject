# Digital Twin — Grinding Circuit BM_001 / CY_001 (Study Project) 🏭⚡

A $0-budget, open-source industrial **Digital Twin of an OCP Phosphate Ore Grinding & Classification Line**, built to mirror a real plant circuit using SysCAD dynamic simulation output (`Dynamic_Results.csv`) and %BPL / Cd granulometric curve data as ground truth.

Master Plan Specification: [digital_twin_grinding_circuit_plan (1).html](file:///home/zakaria/Documents/grindingCircuitProject/digital_twin_grinding_circuit_plan%20%281%29.html)

---

## 📐 Circuit Flowsheet & Topology

The digital twin strictly mirrors the OCP grinding line topology specified in the master plan:

```
  [Slurry_In] ──► [PB_001 Pump Box] ──► [SP_001 Slurry Pump] ──► [BM_001 Ball Mill] ──► [CY_001 Cyclone Cluster] ──► [Slurry_Out]
  (Wash Cyclone)  (Recovers Recycle)    (Feeds Ball Mill)       (160 µm Target)       (Cyclone Overflow)       (Flotation Feed)
                        ▲                                                                    │
                        │                                                                    │ Underflow Recycle
                        └────────────────────────────────────────────────────────────────────┘ (>160 µm Coarse Material)
```

* **Target Cut Point**: $160\,\mu\text{m}$ cyclone cut point target used by OCP for ore quality.
* **Key Quality Metrics**: %BPL (Bone Phosphate of Lime) grade metric and Cadmium (Cd) contaminant concentration.
* **Closed-Loop Recycle**: Coarse hydrocyclone underflow (`CY_001`) recycles back into the pump box (`PB_001`).

---

## 🏗️ 5-Layer Architecture (Zero Budget Stack)

```
  Layer 01 · Data Sources      : SysCAD Dynamic_Results.csv Replay Service + %BPL/Cd Granulometric Curve
  Layer 02 · Edge & Storage    : Mosquitto MQTT Broker + Node-RED + MinIO Object Storage
  Layer 03 · Knowledge & AAS   : Protégé Ontology (.owl) + Neo4j Community DB + Eclipse BaSyx AAS Server & Web UI
  Layer 04 · Visualization     : Ignition Maker Edition (2D Perspective Synoptic) + Blender GLTF + three.js (3D Scene)
  Layer 05 · Apps & Dashboard  : React Dashboard (KPIs, Granulometric Benchmark, Embedded 2D/3D Viewports)
```

---

## 🗺️ Phase Roadmap & Detailed Documentation Index

The project is structured into sequential phases according to the master plan. Comprehensive documentation for each phase is located in the [`/docs`](file:///home/zakaria/Documents/grindingCircuitProject/docs/README.md) directory:

| Phase | Title | Description & Target Deliverables | Detailed Guide |
| :--- | :--- | :--- | :--- |
| **Phase 00** | **Foundation & Team Setup** | Shared git structure, cross-platform `docker-compose.yml` (Ubuntu & Windows parity). | [`docs/PHASE_00_FOUNDATION_TEAM_SETUP.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_00_FOUNDATION_TEAM_SETUP.md) |
| **Phase 01** | **Simulated Live Feed** | Python / Node-RED CSV replay service publishing `Dynamic_Results.csv` to MQTT (`circuit/*`). | [`docs/PHASE_01_SIMULATED_LIVE_FEED.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_01_SIMULATED_LIVE_FEED.md) |
| **Phase 02** | **2D Visualization** | Ignition Maker Edition Perspective synoptic mimic (`PB_001`, `SP_001`, `BM_001`, `CY_001`) with live tag bindings. | [`docs/PHASE_02_2D_VISUALIZATION.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_02_2D_VISUALIZATION.md) |
| **Phase 03** | **3D Visualization** | Blender low-poly GLTF equipment assets animated in three.js canvas via MQTT telemetry. | [`docs/PHASE_03_3D_VISUALIZATION.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_03_3D_VISUALIZATION.md) |
| **Phase 04** | **Knowledge Graph & AAS** | Protégé OWL ontology, Neo4j Community graph, Eclipse BaSyx AAS submodels, circulating load Cypher query. | [`docs/PHASE_04_KNOWLEDGE_GRAPH_AAS.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_04_KNOWLEDGE_GRAPH_AAS.md) |
| **Phase 05** | **Dashboard & KPIs** | Single-pane React dashboard embedding 2D mimic & 3D scene, granulometric benchmark panel, $P_{80}$ deviation alerts. | [`docs/PHASE_05_DASHBOARD_KPIS.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_05_DASHBOARD_KPIS.md) |
| **Phase 06** | **Predictive Maintenance** | **Parked** until Phases 00–05 are stable and validated data exists to avoid GIGO. | [`docs/PHASE_06_PREDICTIVE_MAINTENANCE_PARKED.md`](file:///home/zakaria/Documents/grindingCircuitProject/docs/PHASE_06_PREDICTIVE_MAINTENANCE_PARKED.md) |

---

## 🛠️ Operations & Setup

### Launching Environment
```bash
docker compose up -d
```

### Port Mapping Summary
- **Node-RED Engine**: `http://localhost:1880`
- **Ignition SCADA**: `http://localhost:8088` (Admin: `admin` / `changeme123`)
- **Neo4j Browser**: `http://localhost:7474` (Auth: `neo4j` / `changeme123`)
- **MinIO Console**: `http://localhost:9091` (Auth: `minioadmin` / `minioadmin`)
- **Mosquitto MQTT**: `localhost:1883` (TCP) / `localhost:9001` (WebSockets)
