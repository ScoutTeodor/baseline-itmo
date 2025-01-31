from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MISTRAL_API_KEY: str
    TAVILY_API_KEY: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
