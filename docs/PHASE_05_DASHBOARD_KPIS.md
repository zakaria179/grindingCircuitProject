# Phase 05 — Dashboard & KPIs

* **Status**: Planned (`[ ]`)
* **Master Plan Section**: Section 07 (`#phase5`) in [`digital_twin_grinding_circuit_plan (1).html`](file:///home/zakaria/Documents/grindingCircuitProject/digital_twin_grinding_circuit_plan%20%281%29.html)

---

## 📌 Context & Objective

Phase 05 brings 2D SCADA views, 3D WebGL scenes, and knowledge graph queries together into a single-pane React web application. It provides real-time KPI tiles, granulometric benchmark curves, circulating load metrics, and cut-point deviation alerts.

---

## 🏗️ UI Layout & Panel Components

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       React Operations Dashboard                            │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  Panel 1: Embedded 2D SCADA Mimic   │  Panel 2: Embedded 3D three.js View  │
│  (Ignition Perspective iframe)       │  (WebGL Canvas Component)            │
├──────────────────────────────────────┴──────────────────────────────────────┤
│  Panel 3: Granulometric Benchmark (%BPL / Cd Curve vs Current P80 Marker)    │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  Panel 4: Circulating-Load Tile     │  Panel 5: Equipment Status Cards     │
│  (Neo4j Cypher Query API)            │  (PB_001, SP_001, BM_001, CY_001)    │
├──────────────────────────────────────┴──────────────────────────────────────┤
│  Panel 6: Recharts Live Trend Streams (Solid Flow, %BPL, P80 vs 160µm Target)│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Task List & Component Implementation

### 1. Embedded Viewport Components (`/dashboard`)
- **2D SCADA Panel**: Embeds published Ignition Perspective session (`http://localhost:8088/...`) inside an iframe.
- **3D Scene Panel**: Embeds three.js WebGL canvas component from Phase 03.

### 2. Live Stream Trend Charts (Recharts)
- Render real-time time-series charts per stream subscribing to MQTT WebSockets:
  - Solid mass flow rate ($t/h$)
  - Percent solids concentration (%)
  - %BPL grade and Cadmium (Cd) ppm

### 3. Granulometric Benchmark Panel
- Reproduces OCP's %BPL / Cd / %weight granulometric curve overlay.
- Places a dynamic live marker on the curve showing where current cyclone overflow $P_{80}$ sits relative to the $160\,\mu m$ specification.

### 4. Circulating-Load Tile
- Displays live circulating load percentage calculated via the Neo4j Cypher graph query developed in Phase 04.

### 5. Equipment Status Cards
- Individual operational status cards for `PB_001`, `SP_001`, `BM_001`, and `CY_001` showing run/stopped state, power draw, and last timestamp.

### 6. Cyclone Target Band Alarm Tile
- Visual alert banner triggered whenever cyclone cut point $P_{80}$ drifts outside the $160\,\mu m$ target band.

---

## 📂 Deliverables

- `/dashboard/`: React web application source code.
- **Deliverable**: Dashboard v1 combining KPIs + embedded 2D + embedded 3D.
