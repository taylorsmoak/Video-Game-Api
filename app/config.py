from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_server: str
    database_port: str
    database_name: str

    class Config:
        env_file = '.env'


settings = Settings()
