import os

from langchain_redis import RedisVectorStore


class NewsGroupIndexer:

    @staticmethod
    def index():
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2")

        config = RedisConfig(
            index_name="newsgroups",
            redis_url=os.getenv('REDIS_URL'),  # Todo: Env value obj
            metadata_schema=[{"name": "category", "type": "tag"}]
        )

        vs = RedisVectorStore(embeddings, config=config)

        # ToDo loader