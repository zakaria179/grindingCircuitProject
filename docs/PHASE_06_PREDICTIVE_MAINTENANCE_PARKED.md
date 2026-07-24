# Phase 06 — Predictive Maintenance & Flow Optimization (Parked)

* **Status**: Parked (`[ ]` — PARKED)
* **Master Plan Section**: Section 08 (`#phase6`) in [`digital_twin_grinding_circuit_plan (1).html`](file:///home/zakaria/Documents/grindingCircuitProject/digital_twin_grinding_circuit_plan%20%281%29.html)

---

## 📌 Context & Parked Guardrails

Predictive maintenance and flow optimization are listed as Goals 2 and 3 of the project. However, **Phase 06 is explicitly PARKED** until Phases 00 through 05 run cleanly end-to-end on validated data.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DO NOT START BUILDING                             │
│                                                                             │
│  There is currently no failure/maintenance history and no real sensor stream│
│  — any predictive model built today would be trained on assumptions, not    │
│  evidence (Garbage In, Garbage Out risk).                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ❓ Open Questions to Answer Before Unparking Phase 06

When Phases 00–05 are stable and real or fault-injected datasets are acquired, answer these core questions before starting ML work:

1. **Target Equipment Prioritization**:
   - Should predictive maintenance focus on **`BM_001` (Ball Mill)** first as the highest-value critical asset, or **`SP_001` (Slurry Pump)** as the unit with simpler failure modes (impeller wear/liner breach)?

2. **Practical Scope of Flow Optimization**:
   - What will "flow optimization" adjust in physical practice — setpoints, dilution water addition, cyclone feed pressure, or ball charge ratio?

3. **Data Acquisition Strategy**:
   - Is there any possibility of acquiring informal/anonymized OCP maintenance logs, or must models be trained on structured synthetic fault-injection simulation runs?

---

## 🛠️ Proposed Stack (Future)

- **AutoGluon**: Automated ML for tabular time-series predictive maintenance.
- **Python / Scikit-learn / XGBoost**: Anomaly detection and RUL estimation.
- **n8n**: Workflow automation engine for notification dispatch upon alert triggers.
