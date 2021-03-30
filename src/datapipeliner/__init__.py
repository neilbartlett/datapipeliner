"""
dvc-ready data pipelines
"""

import os

from confuse import LazyConfig

# get config from environment variable or look in cwd by default
ENV_KEY = "DATAPIPELINERDIR"
CONFIG_FILENAME = "config.yaml"
if not os.getenv(ENV_KEY):
    os.environ[ENV_KEY] = os.getcwd()
CONFIG_FOLDERPATH = os.environ[ENV_KEY]
CONFIG = LazyConfig("Datapipeliner", __name__)

from .datapipeliner import Source, Sink, Line  # noqa: E402, F401
