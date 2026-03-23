# Training Models

Models are trained using:

```bash
python -m neural_lam.train_model --config_path <config-path>
```

## Key Training Options

| Option | Description |
|--------|-------------|
| `--config_path` | Path to the Neural-LAM configuration file |
| `--model` | Which model to train (`graph_lam`, `hi_lam`, `hi_lam_parallel`) |
| `--graph` | Which graph to use (e.g. `1level`, `multiscale`, `hierarchical`) |
| `--epochs` | Number of training epochs |
| `--processor_layers` | Number of GNN layers in the processor |
| `--ar_steps_train` | Autoregressive steps during training |

## Available Models

### Graph-LAM
Basic graph-based LAM model. Used for both **L1-LAM** and **GC-LAM**.

### Hi-LAM
Hierarchical version with **sequential** message passing through the mesh hierarchy.

### Hi-LAM-Parallel
All message passing (up, down, inter-level) runs **in parallel**.

## High Performance Computing

Neural-LAM uses PyTorch Lightning's `DDP` backend for distributed training.

### SLURM Example

```bash
#!/bin/bash -l
#SBATCH --job-name=Neural-LAM
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --gres:gpu=4

srun -ul python -m neural_lam.train_model \
    --config_path /path/to/config.yaml \
    --num_nodes $SLURM_JOB_NUM_NODES
```
