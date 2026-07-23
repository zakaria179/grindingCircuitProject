# Phase 04 — Knowledge Graph & Asset Administration Shell (AAS)

The `/graph` directory will house the Industry 4.0 Asset Administration Shell (AAS) metamodel, OWL ontologies, and Neo4j graph database scripts for semantic asset representation of OCP's grinding circuit.

---

## 📌 Planned Architecture & Components

1. **Industry 4.0 Asset Administration Shell (AAS)**:
   * Formal digital representation of grinding assets according to **IDTA (Industrial Digital Twin Association)** standards.
   * **Submodels**:
     - **Nameplate**: Technical specifications, manufacturer info, serial numbers.
     - **Operational Data**: Real-time telemetry bindings, threshold limits (e.g. 160 µm cut point).
     - **Documentation**: Operating manuals, piping & instrumentation diagrams (P&ID).

2. **Neo4j Graph Database**:
   * Storing physical and logical relationships as a property graph:
     ```cypher
     (:Equipment {id: "PB_001"}) -[:FEEDS]-> (:Equipment {id: "SP_001"})
     (:Equipment {id: "SP_001"}) -[:FEEDS]-> (:Equipment {id: "CY_001"})
     (:Equipment {id: "CY_001"}) -[:RECYCLES_UNDERFLOW]-> (:Equipment {id: "PB_001"})
     (:Equipment {id: "CY_001"}) -[:FEEDS_OVERFLOW]-> (:Equipment {id: "Slurry_Out"})
     ```
   * Cypher queries for lineage tracing and root cause impact analysis.

3. **Protégé OWL Ontology**:
   * Semantic domain model mapping equipment classes, material streams, and operational states.
