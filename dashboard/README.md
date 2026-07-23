# Phase 05 — Unified React Monitoring Dashboard

The `/dashboard` directory will contain the single-pane-of-glass web application uniting 2D SCADA views, 3D digital twin canvases, real-time KPI metrics, and knowledge graph insights into a modern React application.

---

## 📌 Planned Scope & Key Features

1. **Technology Stack**:
   * **Framework**: React + Vite + TypeScript
   * **Styling**: Modern CSS design system with HSL variables, dark mode aesthetics, and glassmorphism.
   * **State & Real-time Connectivity**: WebSockets / MQTT connection directly to `mosquitto` (`ws://localhost:9001`).

2. **Core Interface Panels**:
   * **Top KPI Banner**: Circuit throughput (t/h), average output P80 size vs target (160 µm), circulating load ratio %, overall plant status.
   * **Embedded Views**:
     - **2D SCADA Panel**: Embedded Ignition Perspective view.
     - **3D Digital Twin View**: Interactive three.js Canvas for spatial asset inspection.
   * **Equipment Detail Drawer**: Slide-out panel triggered when clicking any asset, displaying live parameters, trend charts (Recharts / Chart.js), and AAS metadata.
