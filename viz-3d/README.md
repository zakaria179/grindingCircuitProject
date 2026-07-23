# Phase 03 — 3D Industrial Visualization (Blender + three.js)

The `/viz-3d` directory will contain the interactive 3D digital twin visualization assets for OCP's phosphate ore grinding circuit.

---

## 📌 Planned Scope & Technical Specifications

1. **3D Asset Modeling (Blender)**:
   * **Low-poly GLTF/GLB models** representing the 4 core equipment pieces:
     - Pump Box (`PB_001`)
     - Slurry Pump (`SP_001`)
     - Ball Mill (`BM_001`)
     - Hydrocyclone Cluster (`CY_001`)
   * Detailed piping network connecting the closed-loop slurry circuit.

2. **Web3D Rendering Engine (three.js)**:
   * **Canvas & Orbit Controls**: Interactive 3D scene embedded in the browser with pan, tilt, zoom, and target focusing on specific equipment.
   * **Real-time Animation & Telemetry Binding**:
     - **Ball Mill Rotation**: Speed of rotation tied to `BM_001` discharge flow rate.
     - **Slurry Flow Particles**: Animated pipe particles visualizing slurry movement direction and flow speed.
     - **Dynamic Material Coloring**: Equipment mesh highlights reflecting operational health (`NORMAL` green, `WARNING` yellow, `CRITICAL` red).

3. **Interactive Raycasting / Selection**:
   * Clicking on any 3D equipment mesh triggers an overlay panel displaying live MQTT metrics from `ocp/grinding/contextualized/{equip_id}`.
