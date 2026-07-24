# Phase 02 — 2D SCADA Visualization & Node-RED Contextualization

## 📌 Executive Summary & Status
* **Status**: `[x] COMPLETED`
* **Target Objective**: Develop real-time data contextualization using Node-RED to derive critical industrial KPIs (recirculating load ratio, $P_{80}$ cut point deviation from 160 µm, and alarm states), and build an interactive 2D SCADA HMI synoptic view in Ignition Maker Edition using the Perspective module.

---

## 🏗️ Architecture & Processing Pipeline

```
  ┌───────────────────────┐
  │   Mosquitto Broker    │ (Raw Telemetry: ocp/grinding/telemetry)
  └───────────┬───────────┘
              │
              ▼
  ┌───────────────────────┐
  │    Node-RED Engine    │ (Port 1880)
  │  - Recirculating Load │
  │  - P80 Deviation      │
  │  - Alarm Thresholds   │
  └───────────┬───────────┘
              │
              ├─────────────────────────────────────────┐
              │ (Enriched KPIs: ocp/grinding/kpi)       │ (Enriched Alarms)
              ▼                                         ▼
  ┌───────────────────────┐                 ┌───────────────────────┐
  │  Ignition Tag Engine  │                 │  Neo4j / React DB     │
  │   (tags.json Export)  │                 │ (Phase 04/05 Consume) │
  └───────────┬───────────┘                 └───────────────────────┘
              │
              ▼
  ┌───────────────────────┐
  │ Ignition Perspective  │
  │  (2D Synoptic HMI)    │ (Port 8088)
  └───────────────────────┘
```

---

## ⚙️ Component Specifications

### 1. Node-RED Contextualization Engine (`http://localhost:1880`)
Node-RED ingests raw JSON streams from `ocp/grinding/telemetry` and performs real-time calculations:
- **Recirculating Load Ratio ($RLR$)**:
  $$RLR = \frac{\text{BM\_001 Discharge Solids }(t/h)}{\text{Fresh Feed Solids Slurry\_In }(t/h)} \times 100\%$$
- **Target $P_{80}$ Deviation ($\Delta P_{80}$)**:
  $$\Delta P_{80} = P_{80,\text{actual}} - 160.0\,\mu\text{m}$$
- **Alarm Rule Evaluation**:
  - `HIGH_P80_WARN`: $P_{80} > 165.0\,\mu\text{m}$ (coarse flotation feed risk).
  - `HIGH_P80_CRIT`: $P_{80} > 175.0\,\mu\text{m}$ (severe cyclone carryover).
  - `HIGH_RECYCLE_WARN`: $RLR > 350\%$ (pump box overflow risk).

Enriched payloads are published back to `ocp/grinding/kpi` and `ocp/grinding/alarms`.

---

### 2. Ignition SCADA Tag Engine & Perspective View (`http://localhost:8088`)

#### A. SCADA Tag Export (`/viz-2d/tags.json`)
Defines structured Tag Providers within Ignition:
- `GrindingCircuit/PB_001/Level` (Memory Tag, Float)
- `GrindingCircuit/SP_001/Flow` (Memory Tag, Float)
- `GrindingCircuit/CY_001/Overflow_P80` (Memory Tag, Float)
- `GrindingCircuit/CY_001/P80_Deviation` (Expression Tag, `{[~]Overflow_P80} - 160.0`)
- `GrindingCircuit/BM_001/Power` (Memory Tag, Float)
- `GrindingCircuit/KPI/RecirculatingLoad` (Memory Tag, Float)

#### B. 2D Perspective Synoptic View (`/viz-2d/flowsheet_perspective_view.json`)
Constructs an interactive vector-graphic HMI representing the OCP grinding flowsheet:
```
  [Slurry_In] ──► [PB_001] ──► [SP_001] ──► [CY_001] ──► [Slurry_Out] (Overflow ≤160µm)
                    ▲                         │
                    │      [BM_001] ◄─────────┘ (Underflow >160µm)
                    └──────────┤
```
- **Dynamic Animations**:
  - Slurry pipe color binding tied to percent solids (dark blue = high density).
  - Hydrocyclone status indicator flashing yellow/red upon $P_{80}$ target deviation.
  - Ball mill dynamic rotation status indicator.

---

## 📋 Commissioning & Import Instructions

### 1. Accessing Ignition Gateway
Navigate to `http://localhost:8088` (Credentials: `admin` / `changeme123`).

### 2. Importing SCADA Tags
1. Open **Ignition Designer** or Gateway Tag Management.
2. Select **Import Tags** and load `/viz-2d/tags.json`.
3. Verify tags update automatically as MQTT streams arrive.

### 3. Importing Perspective View
1. Navigate to **Perspective Views** section.
2. Import `/viz-2d/flowsheet_perspective_view.json`.
3. Launch Perspective Session in web browser to view the active 2D synoptic HMI.

---

## 📂 Repository Artifacts
- `/viz-2d/tags.json`: Ignition Tag Provider JSON schema export.
- `/viz-2d/flowsheet_perspective_view.json`: Ignition Perspective 2D HMI view export.
- `/viz-2d/README.md`: SCADA documentation.
