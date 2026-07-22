# OCP Ore Grinding Circuit Digital Twin

A professional-grade, scalable digital twin of OCP's phosphate ore grinding circuit modeled around a closed-loop flowsheet: `Slurry_In` -> `PB_001` (pump box) -> `SP_001` (centrifugal pump) -> `BM_001` (ball mill, 160 µm target) -> `CY_001` (hydrocyclone cluster, 160 µm cut) -> `Slurry_Out` (to flotation), with `CY_001` underflow recycling back to `PB_001`. Built with a $0 budget using free/open-source tools (Docker, Mosquitto, Neo4j Community, MinIO, Ignition Maker Edition, Blender/three.js), the project focuses on real-time monitoring, AAS knowledge graph representation, and interactive 2D/3D visualization.

> **IMPORTANT**: Before creating or changing anything, read `PROJECT_STATUS.md` first.

---

## Phase Roadmap

- [x] **Phase 00 - Foundation & team setup**
- [ ] **Phase 01 - Pipeline Connection Testing (SysCAD CSV replay -> MQTT)**
- [ ] **Phase 02 - 2D visualization (Ignition Maker Edition, free/non-commercial)**
- [ ] **Phase 03 - 3D visualization (Blender + three.js)**
- [ ] **Phase 04 - Knowledge graph + Asset Administration Shell (Protégé ontology + Neo4j Community + Eclipse BaSyx AAS)**
- [ ] **Phase 05 - Dashboard & KPIs (React, embeds the 2D and 3D views)**
- [ ] **Phase 06 - Predictive maintenance & flow optimization — PARKED**

---

## Prerequisites

- **Windows**: Docker Desktop (See [ZINEB_GUIDE.md](file:///home/zakaria/Documents/grindingCircuitProject/ZINEB_GUIDE.md) for Windows-specific step-by-step setup)
- **Ubuntu**: Docker Engine + Docker Compose (v2+)

---

## Operations

### Start all services
```bash
docker compose up -d
```

### Check service status
```bash
docker compose ps
```

### Stop all services
```bash
docker compose down
```

---

## Service Access URLs

Once services are running (`docker compose up -d`), access the following web interfaces:

- **Neo4j Browser**: [http://localhost:7474](http://localhost:7474) (Credentials: `neo4j` / `changeme123`)
- **MinIO Console**: [http://localhost:9091](http://localhost:9091) (Credentials: `minioadmin` / `minioadmin`)
- **Mosquitto MQTT Broker**: `localhost:1883` (MQTT) / `localhost:9001` (WebSockets) — *Note: Mosquitto has no web UI.*
