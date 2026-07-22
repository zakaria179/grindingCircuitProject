# Zineb's Windows Setup & Execution Guide 🚀

Hi Zineb! This guide is updated after every push to make sure you can safely clone, run, and test the project on **Windows** using Docker Desktop.

---

## 📌 Current Project Status
- **Current Phase**: **Phase 02 - 2D visualization (Ignition Maker Edition)** (Done `[x]`)
- **Services Ready**: Mosquitto (MQTT), Neo4j (Graph DB), MinIO (Object Storage), `replay-service` (SysCAD CSV replay), and Ignition Gateway (`:8088`).

---

## 🛠️ Service Access URLs

| Service | URL | Credentials |
| :--- | :--- | :--- |
| **Ignition SCADA Gateway** (2D HMI) | [http://localhost:8088](http://localhost:8088) | User: `admin`<br>Password: `changeme123` |
| **Neo4j Browser** (Graph DB) | [http://localhost:7474](http://localhost:7474) | User: `neo4j`<br>Password: `changeme123` |
| **MinIO Console** (Object Storage) | [http://localhost:9091](http://localhost:9091) | User: `minioadmin`<br>Password: `minioadmin` |
| **Mosquitto MQTT** | `localhost:1883` (MQTT)<br>`localhost:9001` (WebSockets) | *No Web UI* |

1. **Docker Desktop for Windows**
   - Download & install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
   - Ensure Docker Desktop is **running** (you should see the whale icon in the system tray).
   - *Tip*: Enable WSL 2 backend in Docker Desktop settings if prompted.

2. **Git for Windows** or VS Code / GitHub Desktop.

---

## 🚀 How to Run the Project (Step-by-Step)

### Step 1: Clone or Pull the Repository
Open PowerShell or Command Prompt (or Terminal in VS Code) and run:

```powershell
# If cloning for the first time:
git clone https://github.com/zakaria179/grindingCircuitProject.git
cd grindingCircuitProject

# If you already cloned and want the latest changes:
git pull origin main
```

---

### Step 2: Start All Services with Docker Compose
Run this single command from inside the `grindingCircuitProject` folder:

```powershell
docker compose up -d --build
```
> **What this does**: Docker will automatically pull Mosquitto, Neo4j, and MinIO images, build the `replay-service` container, and start all 4 services in the background.

---

### Step 3: Verify Everything is Running Properly
Check container status:

```powershell
docker compose ps
```
You should see 4 containers in `Up` state (`mosquitto`, `neo4j`, `minio`, `replay-service`).

---

### Step 4: Access the Web Interfaces in Your Browser

Open Chrome, Edge, or Firefox on your computer:

| Service | URL | Credentials |
| :--- | :--- | :--- |
| **Neo4j Browser** (Graph DB) | [http://localhost:7474](http://localhost:7474) | User: `neo4j`<br>Password: `changeme123` |
| **MinIO Console** (Object Storage) | [http://localhost:9091](http://localhost:9091) | User: `minioadmin`<br>Password: `minioadmin` |
| **Mosquitto MQTT** | `localhost:1883` (MQTT)<br>`localhost:9001` (WebSockets) | *No Web UI* |

---

### Step 5: Useful Commands

- **View Live Logs**:
  ```powershell
  docker compose logs -f
  ```
- **Stop All Services Safely**:
  ```powershell
  docker compose down
  ```

---

> 💡 **Note**: Always check `PROJECT_STATUS.md` for the latest roadmap update before building new features!
