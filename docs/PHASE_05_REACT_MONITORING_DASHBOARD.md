# Phase 05 — Unified React Monitoring Dashboard

## 📌 Executive Summary & Status
* **Status**: `[ ] PLANNED`
* **Target Objective**: Build a modern, single-pane-of-glass operations cockpit web application using React + Vite, embedding Ignition 2D SCADA views, three.js 3D canvas, real-time KPI monitoring cards, and historical trend charts.

---

## 🏗️ UI Layout & System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 React Operations Cockpit Dashboard (:3000)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ ┌──────────────────────────┐ ┌──────────────────────────┐ ┌────────────────┐ │
│ │  Ignition 2D Synoptic    │ │    three.js 3D Viewport │ │  Live KPI      │ │
│ │    (iframe :8088)        │ │  (WebGL Canvas :9001)    │ │  Summary Cards │ │
│ └──────────────────────────┘ └──────────────────────────┘ └────────────────┘ │
├─────────────────────────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │                  Recharts Live Telemetry Trend Panel                    │ │
│ │  - Target P80 Deviation (160 µm)  - Recirculating Load %  - Mill Power    │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ Detailed Component Specifications

### 1. Technology Stack (`/dashboard`)
- **Framework**: React 18 + Vite
- **Styling**: Vanilla CSS / CSS Modules with curated industrial dark mode palette
- **Data Visualizations**: Recharts (time-series dynamic charts)
- **Real-time Protocol**: MQTT WebSockets (`paho-mqtt` / `mqtt.js`) listening on `ws://localhost:9001`
- **Embedded Visualizers**:
  - `Ignition2DViewer.jsx`: Embedded iframe pointing to Ignition Perspective Gateway (`http://localhost:8088/data/perspective/client/GrindingCircuit`)
  - `Three3DCanvas.jsx`: WebGL canvas component loading three.js 3D scene from Phase 03

---

### 2. Dashboard Dashboard Components & Feature Set

#### A. Live KPI Summary Cards
- **$P_{80}$ Cut Point Indicator**: Current product particle size vs target $160.0\,\mu\text{m}$. Color-coded badge (Green: $\le 160\,\mu\text{m}$, Red: $> 165\,\mu\text{m}$).
- **Recirculating Load Ratio**: Calculated % ratio derived from Node-RED enriched stream (`ocp/grinding/kpi`).
- **Ball Mill Power Draw**: Live $kW$ draw meter for `BM_001`.
- **Hydrocyclone Pressure**: Live $kPa$ feed pressure for `CY_001`.

#### B. Recharts Telemetry Trend Panel
- Dynamic scrolling time-series line chart tracking:
  - Solid mass flow rate ($t/h$)
  - Percent solids concentration (%)
  - Grade metrics (%BPL, Cadmium ppm)

#### C. Equipment Detail Drawer Component (`EquipmentDrawer.jsx`)
Clicking any equipment item (`PB_001`, `SP_001`, `CY_001`, `BM_001`) opens a slide-out drawer displaying IDTA Asset Administration Shell (AAS) details fetched via REST / Neo4j API.

---

## 📋 Implementation Roadmap

### Step 1: Scaffold React Project
```bash
npx -y create-vite-app@latest ./dashboard --template react
cd dashboard
npm install recharts mqtt lucide-react
```

### Step 2: Component Construction
- Create components in `/dashboard/src/components/`:
  - `Header.jsx`, `KpiCards.jsx`, `IgnitionViewer.jsx`, `ThreeCanvas.jsx`, `TelemetryChart.jsx`, `EquipmentDrawer.jsx`.

### Step 3: MQTT Hook Setup
- Create `/dashboard/src/hooks/useMqttTelemetry.js` handling WebSocket subscription and React state updates.

---

## 📂 Expected Artifacts
- `/dashboard/package.json`: Dependencies & scripts.
- `/dashboard/src/`: React component source code.
- `/dashboard/vite.config.js`: Vite build configuration.
