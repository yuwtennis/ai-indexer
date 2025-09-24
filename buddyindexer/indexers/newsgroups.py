import logging

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_redis import RedisVectorStore, RedisConfig
from sklearn.datasets import fetch_20newsgroups
from sklearn.utils import Bunch

from buddyindexer.settings import NewsGroupsSettings
from buddyindexer.stores.redis import RedisOps


NEWSGROUPS_INDEX = "newsgroups"

class NewsGroupsIndexer:
    LOGGER = logging.getLogger(__name__)

    @staticmethod
    def index():

        categories: list[str] = [
            "alt.atheism", "sci.space"
        ]
        settings = NewsGroupsSettings()
        ops = RedisOps(settings.redis_url)

        newsgroups: Bunch = fetch_20newsgroups(subset='train',
                                        categories=categories, shuffle=True,
                                        random_state=42)

        texts: list[str] = newsgroups.data[:250]
        metadata: list[dict[str, str]] = [
            {"category": newsgroups.target_names[target]} for target in
             newsgroups.target[:250]
        ]

        NewsGroupsIndexer.LOGGER.info('Text size: %d , Metadata size: %d',
                                      len(texts), len(metadata))

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2")

        config = RedisConfig(
            index_name=NEWSGROUPS_INDEX,
            redis_url=settings.redis_url,
            metadata_schema=[{"name": "category", "type": "tag"}]
        )

        vs = RedisVectorStore(embeddings, config=config)

        NewsGroupsIndexer.LOGGER.info('Indexing docs.')
        vs.add_texts(
            texts,
            metadata)