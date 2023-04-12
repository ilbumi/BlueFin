from pydantic import BaseSettings, Field, root_validator


class Settings(BaseSettings):
    db_user: str = Field(..., env="POSTGRES_USER")
    db_password: str = Field(..., env="POSTGRES_PASSWORD")
    db_name: str = Field(..., env="POSTGRES_DB")
    db_server: str = Field(..., env="POSTGRES_SERVER")
    db_port: int = Field(..., env="POSTGRES_PORT")
    db_url: str

    @root_validator(pre=True)
    def fill_database_url(cls, v):
        user = v.get("db_user")
        password = v.get("db_password")
        server = v.get("db_server")
        port = v.get("db_port")
        db = v.get("db_name")

        v["db_url"] = f"postgresql+asyncpg://{user}:{password}@{server}:{port}/{db}"
        return v


settings = Settings()
