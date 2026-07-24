# Phase 03 — 3D Visualization

* **Status**: Planned (`[ ]`)
* **Master Plan Section**: Section 05 (`#phase3`) in [`digital_twin_grinding_circuit_plan (1).html`](file:///home/zakaria/Documents/grindingCircuitProject/digital_twin_grinding_circuit_plan%20%281%29.html)

---

## 📌 Context & Objective

Phase 03 introduces spatial 3D industrial visualization after 2D SCADA monitoring is live and stable. It uses low-poly 3D models created in Blender, loaded into a three.js WebGL canvas, and animated in real time using the exact same MQTT telemetry streams feeding the 2D mimic.

---

## 🏗️ Technical Pipeline & Stack

```
  ┌───────────────────────┐
  │   Blender (Free CAD)  │ ── (Export GLTF / GLB) ──►  ┌───────────────────────┐
  │ Low-Poly Equipment    │                             │    /viz-3d/models/    │
  └───────────────────────┘                             └───────────┬───────────┘
                                                                    │
                                                                    ▼
  ┌───────────────────────┐                             ┌───────────────────────┐
  │   Mosquitto Broker    │ ── (MQTT WebSockets) ─────► │   three.js Viewer     │
  │    Port 9001 (WS)     │         circuit/# topics     │    (WebGL Canvas)     │
  └───────────────────────┘                             └───────────────────────┘
```

---

## 📋 Task List & Implementation Steps

### 1. Equipment Geometry Modeling (Blender)
- Model 4 low-poly, representative equipment items:
  - **`PB_001`**: Pump Box
  - **`SP_001`**: Centrifugal Slurry Pump
  - **`BM_001`**: Ball Mill (160 µm grinding spec)
  - **`CY_001`**: 4-Cyclone Hydrocyclone Cluster
- Export geometry as glTF / GLB binary files to `/viz-3d/models/`.

### 2. three.js Scene Setup (`/viz-3d`)
- Initialize three.js WebGL canvas with OrbitControls and ambient/directional lighting.
- Set up an primary overview camera angle facing the circuit layout.

### 3. MQTT WebSocket Subscriptions
- Connect three.js canvas to Mosquitto WebSocket endpoint (`ws://localhost:9001`).
- Subscribe to `circuit/#` topics (same stream powering Ignition 2D views).

### 4. Telemetry-Driven Motion Animations
- **Ball Mill Rotation**: Rotate `BM_001` mesh on its central axis, scaling RPM based on mill power draw (`circuit/BM_001/power_kw`).
- **Slurry Tint**: Dynamically adjust pipe material color/emissive intensity based on %solids (`circuit/PB_001/percent_solids`).
- **Particle Flow Effects**: Animate basic particle streams along pipe geometry to represent slurry velocity.

---

## ⚠️ Scope Creep Warning

Photoreal 3D modeling is a major time sink with no operational monitoring payoff. Ship **low-poly geometry + correct motion** first; only add visual polish after the 2D + 3D + dashboard loop works end to end.

---

## 📂 Target Deliverables

- `/viz-3d/models/`: glTF asset set for `PB_001`, `SP_001`, `BM_001`, `CY_001`.
- `/viz-3d/index.html`: three.js WebGL viewer page subscribing to MQTT WebSockets.
