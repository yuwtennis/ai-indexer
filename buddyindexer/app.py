import importlib
import traceback

from buddyindexer import indexers
from buddyindexer.settings import Settings


def run():
    try:
        settings = Settings()
        c = getattr(indexers, settings.indexer_name)
        c.index()
    except Exception as e:
        print(repr(traceback.format_exception(e)))