# Phase 06 — Predictive Maintenance & Flow Optimization (Parked)

## 📌 Executive Summary & Status
* **Status**: `[ ] PARKED`
* **Target Objective**: Reserve machine learning (AutoGluon, Scikit-learn) predictive maintenance (PdM) and process flow optimization algorithms for future implementation once empirical sensor failure logs and long-term telemetry histories are available.

---

## 🚫 Parked Rationale & Governance

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       STRICT GOVERNANCE DIRECTIVE                           │
│                                                                             │
│  Phase 06 is explicitly PARKED to prevent Garbage-In, Garbage-Out (GIGO).   │
│  No code shall be committed to /ai-ml until Phases 00–05 are operational.  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Why Phase 06 is Parked
1. **Lack of Industrial Failure Dataset**: Dynamic simulation outputs (`data.csv`) represent nominal process operations without labeled failure events (e.g., slurry pump impeller wear, ball mill liner degradation, cyclone spigot plugging). Training models on unvalidated synthetic failure data produces misleading results.
2. **Monitoring First Principle**: A digital twin must establish accurate, real-time data ingestion, SCADA synoptics, 3D WebGL scenes, and knowledge graphs before layer 5 predictive applications can be built.

---

## 🔮 Future Machine Learning Scope (Once Unparked)

When real plant failure logs or verified fault-injection simulation datasets are acquired, Phase 06 will focus on two core industrial ML tasks:

### 1. Predictive Maintenance (PdM)
- **Target Asset 1 — Slurry Pump (`SP_001`)**: Impeller wear and seal leak detection using vibration and pressure-drop anomaly models.
- **Target Asset 2 — Ball Mill (`BM_001`)**: Liner wear prediction and Remaining Useful Life (RUL) estimation based on power draw fluctuation ($kW$) and sound level acoustics ($dB$).
- **Tooling**: AutoGluon Tabular / TimeSeries, XGBoost, Scikit-learn.

### 2. Closed-Loop Flow Optimization
- **Target KPI**: Maintain hydrocyclone overflow particle size at $P_{80} = 160.0\,\mu\text{m}$ while minimizing specific energy consumption ($kWh/t$).
- **Control Variables**:
  - Pump Box (`PB_001`) dilution water flow rate
  - Slurry Pump (`SP_001`) variable speed drive (VSD) setpoint
  - Hydrocyclone cluster active cyclone count
- **Tooling**: Reinforcement Learning (RL) / Constrained Bayesian Optimization.

---

## 📋 Prerequisites for Unparking Phase 06

1. **Phases 00 through 05 Operational**: All microservices, 2D/3D visualizations, AAS Neo4j graphs, and React dashboards running stably.
2. **Failure Log Acquisition**: Formal or anonymized maintenance logs acquired from OCP, OR structured fault-injection simulation runs generated.
3. **Model Evaluation & Validation**: Verification of model precision/recall metrics against industrial benchmarks before integration.

---

## 📂 Repository Location
- Directory: `/ai-ml` (Currently reserved; contains placeholder README).
