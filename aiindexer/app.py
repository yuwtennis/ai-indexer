import importlib
import traceback

from aiindexer import indexers
from aiindexer.settings import Settings


def run():
    try:
        settings = Settings()
        c = getattr(indexers, settings.indexer_name)
        c.index()
    except Exception as e:
        print(repr(traceback.format_exception(e)))