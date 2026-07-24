# Phase 03 — 3D Industrial Visualization (Blender + three.js)

## 📌 Executive Summary & Status
* **Status**: `[ ] PLANNED`
* **Target Objective**: Build an interactive, spatial 3D WebGL scene of the OCP grinding circuit using low-poly models created in Blender and rendered via three.js, animated in real time by telemetry streaming over MQTT WebSockets.

---

## 🏗️ Technical Architecture & Pipeline

```
  ┌───────────────────────┐
  │   Blender 4.x CAD     │ ── (Export GLTF / GLB) ──►  ┌───────────────────────┐
  │ (PB_001, SP_001, etc.)│                             │   /viz-3d/models/     │
  └───────────────────────┘                             └───────────┬───────────┘
                                                                    │
                                                                    ▼
  ┌───────────────────────┐                             ┌───────────────────────┐
  │   Mosquitto Broker    │ ── (MQTT WebSockets) ─────► │   three.js Canvas     │
  │    Port 9001 (WS)     │      ocp/grinding/telemetry │  (WebGL 3D Scene)     │
  └───────────────────────┘                             └───────────────────────┘
```

---

## ⚙️ Detailed Implementation Specifications

### 1. 3D Asset Modeling Guidelines (Blender)
* **Directory**: `/viz-3d/models/`
* **Asset Library Requirements**:
  - `PB_001.gltf`: Pump Box receiving fresh feed and recycle slurry.
  - `SP_001.gltf`: Centrifugal Slurry Pump with drive motor.
  - `CY_001.gltf`: 4-Cyclone Hydrocyclone Cluster with distributor header.
  - `BM_001.gltf`: Industrial Ball Mill with girth gear, pinion, and discharge trunnion.
  - `piping_assembly.gltf`: Interconnecting slurry pipes.
* **Optimization Budget**: Max 50,000 total polygons for the entire scene; GLB file sizes $< 5.0\,\text{MB}$.

---

### 2. three.js WebGL Scene Implementation (`/viz-3d`)

#### A. Core Components
- `index.html`: WebGL container canvas and controls overlay.
- `src/scene.js`: Scene setup (PerspectiveCamera, DirectionalLight, AmbientLight, OrbitControls).
- `src/loader.js`: GLTFLoader parsing `/viz-3d/models/*.gltf`.
- `src/mqtt-connector.js`: Paho MQTT JS client connecting to `ws://localhost:9001`.

#### B. Telemetry-Driven Motion Bindings

| Equipment / Component | MQTT Telemetry Tag | 3D Visual Animation / Shader Effect |
| :--- | :--- | :--- |
| **`BM_001` (Ball Mill)** | `mill_power_kw` | Y-axis mesh rotation: $\text{RPM} = \frac{\text{power\_kw}}{1500} \times 15.0$ |
| **`SP_001` (Slurry Pump)** | `slurry_flow_m3h` | Impeller motor rotation speed scaling with flow |
| **Slurry Pipe Streams** | `volumetric_flow_m3h` | Particle system velocity along spline curves |
| **`CY_001` Hydrocyclone** | `overflow_p80` | Emissive material tint (Green: $\le 160\,\mu\text{m}$, Red: $> 165\,\mu\text{m}$) |

---

## 📋 Step-by-Step Implementation Roadmap

### Step 1: Geometry Export
1. Model low-poly meshes in Blender.
2. Export as binary `.glb` to `/viz-3d/models/`.

### Step 2: Canvas Development
1. Initialize three.js scene with OrbitControls.
2. Load GLB assets and position according to circuit topology.

### Step 3: MQTT Integration
1. Connect via WebSockets (`ws://localhost:9001`).
2. Subscribe to `ocp/grinding/telemetry`.
3. Update mesh rotations and material colors in the `requestAnimationFrame()` render loop.

---

## 📂 Expected Artifacts
- `/viz-3d/models/`: GLTF / GLB equipment models.
- `/viz-3d/index.html`: Entry HTML page for 3D visualization.
- `/viz-3d/src/`: JS source files for three.js rendering and MQTT handling.
