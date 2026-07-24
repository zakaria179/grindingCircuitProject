# Phase 00 — Foundation & Microservices Infrastructure

## 📌 Executive Summary & Status
* **Status**: `[x] COMPLETED`
* **Target Objective**: Establish a containerized, reproducible microservice infrastructure for the Digital Twin of OCP's Ore Grinding Circuit, ensuring $0 software budget compliance and seamless cross-platform execution on Ubuntu Linux and Windows (Docker Desktop).

---

## 🏗️ System Architecture & Services Breakdown

The foundation orchestrates **6 core microservices** via a unified `docker-compose.yml` specification:

```
                      ┌──────────────────────────────────────────┐
                      │             docker-compose               │
                      └────────────────────┬─────────────────────┘
                                           │
  ┌─────────────────┬──────────────────┼──────────────────┬─────────────────┬────────────────┐
  │                 │                  │                  │                 │                │
  ▼                 ▼                  ▼                  ▼                 ▼                ▼
[mosquitto]     [neo4j]             [minio]        [replay-service]   [ignition]     [node-red]
 (MQTT Spine)  (Graph DB)       (Object Store)      (Telemetry Gen)   (2D SCADA)    (KPI Engine)
:1883 / :9001  :7474 / :7687    :9000 / :9091           (Internal)       :8088           :1880
```

### 1. Services Configuration Matrix

| Service Container | Image / Build | Published Ports | Persistent Volumes | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **`mosquitto`** | `eclipse-mosquitto:latest` | `1883:1883`<br>`9001:9001` | Config bind: `./broker/mosquitto.conf` | Central MQTT message broker routing live process telemetry across TCP (1883) and WebSockets (9001). |
| **`neo4j`** | `neo4j:community` | `7474:7474`<br>`7687:7687` | Volume: `neo4j_data` | Property graph database storing Industry 4.0 Asset Administration Shell (AAS) topologies and Cypher queries. |
| **`minio`** | `minio/minio:latest` | `9000:9000`<br>`9091:9001` | Volume: `minio_data` | High-performance object storage for GLTF 3D assets, CSV raw exports, and assay benchmark files. |
| **`replay-service`** | Build: `./replay-service` | *Internal* | None | Python microservice streaming 482 rows of continuous SysCAD industrial grinding simulation data. |
| **`ignition`** | `kcollins/ignition:8.1.33` | `8088:8088`<br>`8043:8043` | Volume: `ignition_data` | Industrial SCADA HMI gateway hosting Perspective 2D synoptic views and SCADA tag providers. |
| **`node-red`** | `nodered/node-red:latest` | `1880:1880` | Volume: `nodered_data` | Data contextualization engine computing recirculating loads, target $P_{80}$ cut point deviations, and alarm states. |

---

## 🛠️ Configuration Details

### Mosquitto Configuration (`/broker/mosquitto.conf`)
```ini
listener 1883
allow_anonymous true

listener 9001
protocol websockets
allow_anonymous true
```

### Docker Compose Specifications (`docker-compose.yml`)
- All services belong to the default bridge network (`grindingcircuitproject_default`).
- Health checks and automatic restart policies (`restart: unless-stopped`) guarantee high availability.
- Environment credentials configured for dev environment (`admin/changeme123`, `neo4j/changeme123`, `minioadmin/minioadmin`).

---

## 📋 Verification & Operational Guide

### 1. Launching All Services
```bash
docker compose up -d
```

### 2. Validating Container Health
```bash
docker compose ps
```
*Expected Output*: All 6 containers showing `State: Up`.

### 3. Port Accessibility Checks
- **Mosquitto MQTT**: `localhost:1883` (TCP) / `localhost:9001` (WebSocket)
- **Node-RED**: `http://localhost:1880`
- **Ignition SCADA**: `http://localhost:8088`
- **Neo4j Browser**: `http://localhost:7474`
- **MinIO Console**: `http://localhost:9091`

---

## 📂 Repository Artifacts
- `docker-compose.yml`: Master multi-container orchestrator.
- `/broker/mosquitto.conf`: MQTT protocol configuration file.
- `README.md`: Central repository documentation.
- `ZINEB_GUIDE.md`: Step-by-step developer guide for Windows Docker Desktop users.
- `PROJECT_STATUS.md`: Phase state single source of truth.
