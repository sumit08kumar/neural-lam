# Evaluation and Logging

## Evaluating Models

```bash
python -m neural_lam.train_model --config_path <config-path> --eval <split>
```

Use `--eval val` for validation set or `--eval test` for test data.

### Key Evaluation Options

| Option | Description |
|--------|-------------|
| `--load` | Path to model checkpoint (`.ckpt`) to load |
| `--n_example_pred` | Number of example predictions to plot |
| `--ar_steps_eval` | Number of autoregressive steps to unroll |

:::{warning}
Using multiple GPUs for evaluation is **strongly discouraged**. The
`DistributedSampler` replicates samples to equalize batch sizes, making
evaluation metrics unreliable.
:::

## Logging

### Weights & Biases
Neural-LAM is fully integrated with [W&B](https://www.wandb.ai/) for tracking.

### MLFlow
[MLFlow](https://mlflow.org/) integration is also available:
```bash
MLFLOW_TRACKING_URI=http://localhost:5000 \
    python -m neural_lam.train_model \
    --config_path <config_path> --logger mlflow
```

## Metrics

| Metric | Description |
|--------|-------------|
| MSE | Mean Squared Error |
| MAE | Mean Absolute Error |
| WMSE | Weighted MSE |
| NLL | Negative Log Likelihood |
| CRPS | Continuous Ranked Probability Score |
