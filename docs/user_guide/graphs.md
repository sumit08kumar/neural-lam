# Graph Creation

Neural-LAM uses graph structures to define message-passing GNN layers that
emulate fluid flow in the atmosphere.

## Creating Graphs

```bash
python -m neural_lam.create_graph --config_path <neural-lam-config-path> --name <graph-name>
```

Run `python -m neural_lam.create_graph --help` for a full list of options.

### Graph Types

**GC-LAM** (multi-scale mesh):
```bash
python -m neural_lam.create_graph --config_path <config-path> --name multiscale
```

**Hi-LAM / Hi-LAM-Parallel** (hierarchical mesh):
```bash
python -m neural_lam.create_graph --config_path <config-path> --name hierarchical --hierarchical
```

**L1-LAM** (single-level mesh):
```bash
python -m neural_lam.create_graph --config_path <config-path> --name 1level --levels 1
```

## Graph Directory Structure

```
graphs/
├── graph1/
│   ├── m2m_edge_index.pt       - Mesh-to-mesh edges
│   ├── g2m_edge_index.pt       - Grid-to-mesh edges
│   ├── m2g_edge_index.pt       - Mesh-to-grid edges
│   ├── m2m_features.pt         - Mesh edge features
│   ├── g2m_features.pt         - Grid-to-mesh edge features
│   ├── m2g_features.pt         - Mesh-to-grid edge features
│   └── mesh_features.pt        - Mesh node features
└── ...
```

## Mesh Hierarchy

For hierarchical graphs (`L > 1` levels), files like `m2m_edge_index.pt`,
`m2m_features.pt`, and `mesh_features.pt` contain **lists of length `L`**, where
each entry corresponds to a level (index 0 = lowest level).
