from pydantic import BaseSettings

class Settings(BaseSettings):
    firebase_key_path: str

    class Config:
        env_file = ".env"

settings = Settings()
