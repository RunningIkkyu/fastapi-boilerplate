from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False, env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    # Database settings
    db_host: str = "127.0.0.1"
    db_port: int = 3306
    db_user: str = "root"
    db_password: str = ""
    db_name: str = Field(default="", min_length=1)
    # Milvus Settings
    milvus_host: str = Field(default="127.0.0.1")
    milvus_port: str = Field(default="19530")
    milvus_collection_name: str = Field(default="milvus_collection")
    milvus_hard_material_collection_name: str = Field(
        default="milvus_hard_material_collection"
    )
    milvus_search_limit: str = Field(default="10")
    hard_material_search_limit: str = Field(default="10")
    # Sentry Settings
    sentry_dsn_worker: str = Field(default="", min_length=1)
    sentry_dsn_api: str = Field(default="", min_length=1)
    sentry_env: str = Field(default="", min_length=1)


settings = Settings()
