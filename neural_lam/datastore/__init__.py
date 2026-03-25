"""Datastore implementations for loading weather data."""
# Local
from .base import BaseDatastore  # noqa
from .mdp import MDPDatastore  # noqa
from .npyfilesmeps import NpyFilesDatastoreMEPS  # noqa

DATASTORE_CLASSES = [
    MDPDatastore,
    NpyFilesDatastoreMEPS,
]

DATASTORES = {
    datastore.SHORT_NAME: datastore  # type: ignore
    for datastore in DATASTORE_CLASSES
}


def init_datastore(datastore_kind, config_path):
    """
    Initialize a datastore of the given kind.

    Parameters
    ----------
    datastore_kind : str
        The kind of datastore to initialize.
    config_path : str
        The path to the configuration file for the datastore.

    Returns
    -------
    BaseDatastore
        The initialized datastore.
    """
    DatastoreClass = DATASTORES.get(datastore_kind)

    if DatastoreClass is None:
        raise NotImplementedError(
            f"Datastore kind {datastore_kind} is not implemented"
        )

    datastore = DatastoreClass(config_path=config_path)

    return datastore
