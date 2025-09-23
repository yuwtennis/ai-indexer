# buddy-indexer

## Sample index scenarios

- Newsgroup. This is a example from the redis vector store in [langchain doc](https://python.langchain.com/docs/integrations/vectorstores/redis/#what-is-redis)

## Stores

- redis

## How to

### Build your store

```shell
docker build -t vs-redis:latest . 
```

### Run your store

```shell
docker run -p 6379:6379 vs-redis:latest 
```