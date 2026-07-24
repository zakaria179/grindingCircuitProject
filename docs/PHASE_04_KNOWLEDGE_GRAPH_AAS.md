# Phase 04 — Knowledge Graph & Asset Administration Shell (AAS)

* **Status**: Planned (`[ ]`)
* **Master Plan Section**: Section 06 (`#phase4`) in [`digital_twin_grinding_circuit_plan (1).html`](file:///home/zakaria/Documents/grindingCircuitProject/digital_twin_grinding_circuit_plan%20%281%29.html)

---

## 📌 Context & Objective

Phase 04 establishes the single source of truth for plant topology, equipment metadata, and Industry 4.0 Asset Administration Shell (AAS) digital nameplates. Using **Protégé**, **Neo4j Community**, and **Eclipse BaSyx**, it models the closed-loop relationships of the grinding circuit so that circulating loads and fault propagation can be traversed as a property graph rather than a flat tag list.

---

## 🏗️ Architecture & Component Stack

```
                   ┌─────────────────────────────────────────┐
                   │           Protégé Ontology              │
                   │        (grinding_ontology.owl)          │
                   └────────────────────┬────────────────────┘
                                        │
                                        ▼
                   ┌─────────────────────────────────────────┐
                   │           Neo4j Community DB            │
                   │         (Ports 7474 / 7687)             │
                   └────────────────────┬────────────────────┘
                                        │
         ┌──────────────────────────────┼──────────────────────────────┐
         ▼                              ▼                              ▼
  [AAS Submodels]              [Eclipse BaSyx Server]         [Cypher Queries]
  - Nameplates                 - AAS Web UI                   - Circulating Load Ratio
  - Design Specs               - Live Metadata Editor         - Closed-Loop Traversal
```

---

## 📋 Task List & Implementation Steps

### 1. Protégé Ontology Modeling (`/graph/grinding_ontology.owl`)
- Define OWL Ontology classes:
  - `Equipment` (Subclasses: `Pump`, `PumpBox`, `Mill`, `CycloneCluster`)
  - `Stream`
  - `Property`
- Define object properties: `feeds`, `discharges_to`, `recycles_to`.

### 2. Topology Graph Population (Neo4j Community)
Encode the closed-loop circuit topology in Neo4j using Cypher:
```cypher
// Circuit Closed Loop Topology
(PB_001:Equipment {id: 'PB_001', name: 'Pump Box'})-[:FEEDS]->(SP_001:Equipment {id: 'SP_001', name: 'Slurry Pump'})
(SP_001:Equipment)-[:FEEDS]->(BM_001:Equipment {id: 'BM_001', name: 'Ball Mill'})
(BM_001:Equipment)-[:DISCHARGES_TO]->(CY_001:Equipment {id: 'CY_001', name: 'Cyclone Cluster'})
(CY_001:Equipment)-[:RECYCLES_TO]->(PB_001:Equipment)
(CY_001:Equipment)-[:DISCHARGES_TO]->(Slurry_Out:Stream {name: 'Flotation Feed'})
```

### 3. Eclipse BaSyx AAS Server & Web UI
- Deploy Eclipse BaSyx AAS container and AAS Web UI.
- Create 4 AAS submodels (`PB_001`, `SP_001`, `BM_001`, `CY_001`) storing:
  - Digital Nameplate specs (mill diameter, cyclone cut size $160\,\mu m$).
  - Operational parameters.
  - Linked engineering documents (flowsheet PDF, Blender 3D GLTF asset links).
- Enable AAS Web UI for editing metadata without modifying raw graph code.

### 4. Circulating Load Ratio Cypher Query
Authored for consumption by the Phase 05 React dashboard:
```cypher
MATCH (bm:Equipment {id: 'BM_001'})-[:DISCHARGES_TO]->(cy:Equipment {id: 'CY_001'})-[:RECYCLES_TO]->(pb:Equipment {id: 'PB_001'})
MATCH (feed:Stream {name: 'Slurry_In'})-[:FEEDS]->(pb)
RETURN (bm.solids_tph / feed.solids_tph) * 100.0 AS CirculatingLoadRatio;
```

---

## 📂 Deliverables

- `/graph/grinding_ontology.owl`: Protégé ontology file.
- `/graph/schema.cypher`: Populated Neo4j property graph script.
- 4 Eclipse BaSyx AAS Submodel JSON configurations.
- Working Cypher circulating load calculation query.
