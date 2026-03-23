# Data: DataStores and WeatherDataset

Neural-LAM uses a two-part data representation for flexibility:

1. **DataStore** — loads data from disk and returns `xarray.DataArray` objects
2. **WeatherDataset** — a PyTorch `Dataset` that samples in time, normalizes, and produces tensors

## DataStore Architecture

A datastore (subclass of `BaseDatastore`) handles loading a given category
(`state`, `forcing`, or `static`) and split (`train`/`val`/`test`) of data.
The returned data-array has:

- Spatial coordinates flattened into a single `grid_index` dimension
- All variables and vertical levels stacked into a `{category}_feature` dimension

The datastore also provides:
- Variable names, long names, and units
- Boundary mask
- Normalization statistics (mean and std)
- Grid coordinate information

## Available DataStores

### MDPDatastore (`mllam-data-prep`)

`MDPDatastore` loads *training-ready* datasets in zarr format created with
[mllam-data-prep](https://github.com/mllam/mllam-data-prep).

**Running preprocessing:**

```bash
# Basic usage
python -m mllam_data_prep --config data/danra.datastore.yaml

# Parallel processing for large datasets (≥10GB)
python -m mllam_data_prep --config data/danra.datastore.yaml \
    --dask-distributed-local-core-fraction 0.5
```

### NpyFilesDatastoreMEPS

Reads MEPS data from `.npy` files in the format from neural-lam `v0.1.0`.

:::{note}
This datastore is specific to the MEPS dataset format but can serve as an example
for similar numpy-based datastores.
:::

**Standardization (required for npy-file datastores):**

```bash
python -m neural_lam.datastore.npyfilesmeps.compute_standardization_stats <path-to-datastore-config>
```

### Custom DataStores

Create your own by subclassing `BaseDatastore` or `BaseRegularGridDatastore`.

## WeatherDataset

The `WeatherDataset` class takes a datastore and handles temporal sampling,
normalization, and conversion to `torch.Tensor` objects.
The companion `WeatherDataModule` (PyTorch Lightning `LightningDataModule`)
manages train/val/test dataloaders.
