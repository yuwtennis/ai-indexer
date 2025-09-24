# buddy-indexer

## Sample index scenarios

- Newsgroups. This is a example from the redis vector store in [langchain 
  doc](https://python.langchain.com/docs/integrations/vectorstores/redis/#what-is-redis)

## Stores

- redis

## How to

### Build your store

e.g. Build vector store of redis
```shell
docker build -t vs-redis:latest . 
```

### Run your store

e.g. Sping up redis
```shell
export REDIS_URL="redis://localhost:6379"

docker run -p 6379:6379 vs-redis:latest 
```

### Load data to store

e.g. Load vector store using indexer NewsGroupsIndexer
```shell
export INDEXER_NAME=NewsGroupsIndexer

poetry run python3 __main__.py
```