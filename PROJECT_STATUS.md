# Grinding Circuit Project — Status & Roadmap

This file is the single source of truth for the project build status. Always check this file before creating or modifying code, and update it upon completing work.

---

## Project Phase Roadmap

- [x] **Phase 00 - Foundation & team setup**
  - **Status**: [x] Done
  - **What exists right now**:
    - Complete folder structure (`/broker`, `/replay-service`, `/graph`, `/viz-2d`, `/viz-3d`, `/dashboard`, `/ai-ml`)
    - `/ai-ml/README.md` (Parked placeholder for Phase 06)
    - `/broker/mosquitto.conf` (Mosquitto MQTT configuration for dev)
    - `/replay-service/Dockerfile`, `requirements.txt`, `main.py` (Placeholder container setup)
    - `docker-compose.yml` (Orchestrates Mosquitto, Neo4j, MinIO, and replay-service)
    - `README.md` (Project overview, roadmap, and running instructions)
    - `ZINEB_GUIDE.md` (Windows setup & execution guide for team member Zineb)
    - `PROJECT_STATUS.md` (Single source of truth for project status)
    - Empirical Docker verification passed cleanly (`docker compose up -d` & `docker compose ps` showed 4 containers running; HTTP 200 responses verified for Neo4j at `:7474` and MinIO at `:9091`). Containers stopped cleanly via `docker compose down`.

- [x] **Phase 01 - Pipeline Connection Testing (SysCAD CSV replay -> MQTT)**
  - **Status**: [x] Done
  - **What exists right now**: `replay-service` with `data.csv` (482 SysCAD readings dataset) and Python MQTT replay service (`main.py`) streaming telemetry live to Mosquitto MQTT topics (`ocp/grinding/telemetry` & equipment-specific topics). Verified via container logs.

- [ ] **Phase 02 - 2D visualization (Ignition Maker Edition, free/non-commercial)**
  - **Status**: [ ] Not Started
  - **What exists right now**: Empty `/viz-2d` directory.

- [ ] **Phase 03 - 3D visualization (Blender + three.js)**
  - **Status**: [ ] Not Started
  - **What exists right now**: Empty `/viz-3d` directory.

- [ ] **Phase 04 - Knowledge graph + Asset Administration Shell (Protégé ontology + Neo4j Community + Eclipse BaSyx AAS)**
  - **Status**: [ ] Not Started
  - **What exists right now**: Empty `/graph` directory. Neo4j container configured in Compose.

- [ ] **Phase 05 - Dashboard & KPIs (React, embeds the 2D and 3D views)**
  - **Status**: [ ] Not Started
  - **What exists right now**: Empty `/dashboard` directory.

- [ ] **Phase 06 - Predictive maintenance & flow optimization — PARKED**
  - **Status**: [ ] Not Started (PARKED)
  - **What exists right now**: `/ai-ml/README.md` stating Phase 06 is parked until realistic sensor failure data is available. Do not create code here.
