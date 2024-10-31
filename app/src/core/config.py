import os
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables
load_dotenv()


class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str
    PROJECT_NAME: str

    # Vector DB Settings
    QDRANT_HOST: str
    QDRANT_PORT: int
    COLLECTION_NAME: str

    # Model Settings
    MODEL_NAME: str
    EMBEDDING_MODEL: str
    MAX_LENGTH: int

    # LangSmith Settings
    LANGCHAIN_TRACING_V2: str
    LANGCHAIN_ENDPOINT: str
    LANGCHAIN_API_KEY: Optional[str]
    LANGCHAIN_PROJECT: str

    # Hugging Face Settings
    HUGGINGFACE_TOKEN: str

    class Config:
        env_file = ".env"
        case_sensitive = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        env_vars = [
            ("API_V1_STR", ""),
            ("PROJECT_NAME", ""),
            ("QDRANT_HOST", ""),
            ("QDRANT_PORT", "0", int),
            ("COLLECTION_NAME", ""),
            ("MODEL_NAME", ""),
            ("EMBEDDING_MODEL", ""),
            ("MAX_LENGTH", "0", int),
            ("LANGCHAIN_TRACING_V2", ""),
            ("LANGCHAIN_ENDPOINT", ""),
            ("LANGCHAIN_API_KEY", None),
            ("LANGCHAIN_PROJECT", ""),
        ]

        for var in env_vars:
            name, default, *transform = var
            value = os.getenv(name, default)
            if transform:
                value = transform[0](value)
            setattr(self, name, value)
            if not value and name != "LANGCHAIN_API_KEY":
                print(f"{name} not found in .env")


# Initialize settings
settings = Settings()
