# Phase 02 — 2D Visualization

* **Status**: Completed (`[x]`)
* **Master Plan Section**: Section 04 (`#phase2`) in [`digital_twin_grinding_circuit_plan (1).html`](file:///home/zakaria/Documents/grindingCircuitProject/digital_twin_grinding_circuit_plan%20%281%29.html)

---

## 📌 Context & Objective

Phase 02 builds an interactive 2D SCADA HMI flowsheet mimic using **Ignition Maker Edition** (Perspective module). It translates MQTT telemetry streams into real-time visual pipe animations, grade call-outs, $P_{80}$ target band indicators, and alarm states.

---

## 🛠️ Step-by-Step Implementation Roadmap

```
Step 1: Install & Commission Ignition Gateway (Maker Edition)
  │
  ▼
Step 2: Connect MQTT Engine / OPC-UA to Mosquitto Broker (:1883)
  │
  ▼
Step 3: Redraw Static Flowsheet (PB_001 → SP_001 → BM_001 → CY_001)
  │
  ▼
Step 4: Bind Milestone Tag (Pipe Color/Opacity tied to %solids)
  │
  ▼
Step 5: Finish Bindings (Flow Animations, %BPL/P80 Call-outs, 160µm Cut Band, Alarms)
  │
  ▼
Step 6: Publish Perspective Session (Embeddable iframe for Phase 05 React Dashboard)
```

---

## ⚙️ Detailed Execution Steps

### Step 1 — Gateway Commissioning
- Deployed Ignition Gateway container (`kcollins/ignition:8.1.33`) on port `8088`.
- Commissioned as **Ignition Maker Edition** (free for non-commercial/educational use).

### Step 2 — Data Connection
- Configured MQTT Engine module pointing to Mosquitto container (`mqtt://mosquitto:1883`).
- Subscribed to `circuit/#` topic namespace.

### Step 3 — Static Flowsheet Drawing
- Created Perspective View representing the 4 core equipment items and 6 interconnecting slurry streams:
  - `Slurry_In` ➔ `PB_001` (Pump Box)
  - `PB_001` ➔ `SP_001` (Slurry Pump)
  - `SP_001` ➔ `BM_001` (Ball Mill)
  - `BM_001` ➔ `CY_001` (Cyclone Cluster)
  - `CY_001` Overflow ➔ `Slurry_Out` (Flotation Feed)
  - `CY_001` Underflow ➔ Recycle back to `PB_001`

### Step 4 — Milestone Tag Binding
- Bound pipe fill color dynamically to `circuit/PB_001/percent_solids` (darker tint = higher slurry concentration).

### Step 5 — Comprehensive Bindings & Target Band
- **Flow Animation**: Added dynamic stroke dash-array movement to active slurry pipes.
- **Value Call-outs**: Real-time display panels for %BPL grade and $P_{80}$ particle size.
- **Target-Band Color Bar**: Visual status bar on `CY_001` indicating proximity to the $160\,\mu m$ OCP target cut point.
  - Green: $P_{80} \le 160\,\mu m$
  - Amber Warning: $160\,\mu m < P_{80} \le 165\,\mu m$
  - Red Alarm: $P_{80} > 165\,\mu m$

### Step 6 — Browser Session Publishing
- Published Perspective session URL (`http://localhost:8088/data/perspective/client/GrindingCircuit`), ready for iframe embedding in the Phase 05 React dashboard.

---

## 📂 Repository Deliverables

- `/viz-2d/tags.json`: Ignition Tag Provider JSON schema export.
- `/viz-2d/flowsheet_perspective_view.json`: Ignition Perspective HMI view file.
- `/viz-2d/README.md`: Ignition setup instructions.
