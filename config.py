from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""
    
    # User profile information
    user_email: str = "gwinsetech@gmail.com"
    user_name: str = "Godwin Sunday Ekpoesu"
    user_stack: str = "Python/FastAPI"
    
    # External API configuration
    cat_facts_api_url: str = "https://catfact.ninja/fact"
    api_timeout: int = 5  # seconds
    
    # Server configuration
    app_name: str = "Dynamic Profile Endpoint"
    app_version: str = "1.0.0"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()

