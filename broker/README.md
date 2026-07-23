# Broker — Eclipse Mosquitto MQTT Infrastructure

The `/broker` directory contains the configuration files for the **Eclipse Mosquitto MQTT Broker**, which acts as the central real-time messaging spine for the OCP Grinding Circuit Digital Twin.

---

## 📌 Architecture & Topic Hierarchy

Mosquitto routes telemetry between data producers (`replay-service`), middleware contextualizers (`node-red`), and visualizers (`ignition`, `viz-3d`, `dashboard`).

### Topic Structure

| Topic Pattern | Description | Producer | Consumer |
| :--- | :--- | :--- | :--- |
| `ocp/grinding/telemetry` | Raw full dataset telemetry stream | `replay-service` | Node-RED, MinIO logger |
| `ocp/grinding/equipment/{equip_id}` | Segmented per-equipment raw metrics | `replay-service` | Ignition SCADA, Node-RED |
| `ocp/grinding/contextualized/{equip_id}` | Enriched asset metrics with KPI alarms & health status | `node-red` | Ignition SCADA, React Dashboard |
| `ocp/grinding/events/alarms` | Real-time threshold alarm triggers | `node-red` | React Dashboard, Ignition |

---

## 🛠️ Configuration Details (`mosquitto.conf`)

* **Listener Port 1883**: Unencrypted standard MQTT protocol for inter-container communication.
* **Listener Port 9001**: WebSockets listener enabling direct browser-based subscriptions for web dashboards.
* **Anonymous Access**: Enabled for local development environments.
