from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    indexer_name: str

class NewsGroupsSettings(Settings):
    redis_url: str