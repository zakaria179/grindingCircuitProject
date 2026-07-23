# Zineb's Windows Setup & Execution Guide 🚀

Hi Zineb! This guide is updated after every push to make sure you can safely clone, run, and test the project on **Windows** using Docker Desktop.

---

## 📌 Current Project Status & Architecture

- **Current Completed Phase**: **Phase 02 — 2D Visualization & Node-RED Integration** (`[x]`)
- **Active Microservices**:
  1. `mosquitto`: MQTT messaging broker (`:1883`)
  2. `replay-service`: Streams live SysCAD telemetry from `data.csv`
  3. `node-red`: Data integration & contextualization engine (`:1880`)
  4. `ignition`: Industrial 2D SCADA HMI gateway (`:8088`)
  5. `neo4j`: AAS Knowledge Graph database (`:7474`)
  6. `minio`: Object storage console (`:9091`)

---

## 🌐 Quick Access Links & Web Interfaces

Once containers are running via Docker Desktop, open your web browser and navigate to:

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
2. If prompted, make sure WSL 2 backend is enabled.

### Step 2: Open Terminal / VS Code & Pull Latest Changes
Open PowerShell, Command Prompt, or VS Code terminal in your project directory:

```powershell
git pull origin main
```

### Step 3: Launch All Microservices
Run the following command to build and launch all containers in background mode:

```powershell
docker compose up -d
```

### Step 4: Verify Container Status
Check that all containers show as `Up`:

```powershell
docker compose ps
```

### Step 5: Test Web Interfaces
1. Open **Node-RED** at [http://localhost:1880](http://localhost:1880). You can build drag-and-drop flows to compute KPIs or format MQTT telemetry!
2. Open **Ignition** at [http://localhost:8088](http://localhost:8088). Login with `admin` / `changeme123` to inspect Tag Providers and Perspective 2D Views.

---

## 💻 Working with Git (Making & Pushing Changes)

When you make changes or add new files on your machine, follow these commands to push them back to the repository:

1. **Check changed files**:
   ```powershell
   git status
   ```

2. **Stage your changes**:
   ```powershell
   git add .
   ```

3. **Commit your work with a clear message**:
   ```powershell
   git commit -m "Your description of work done"
   ```

4. **Push to GitHub**:
   ```powershell
   git push origin main
   ```

If you encounter any issues or Docker errors on Windows, let the team know!
