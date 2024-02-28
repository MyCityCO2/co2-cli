from pathlib import Path

import typer
from pydantic import model_validator
from pydantic_settings import BaseSettings

from co2.utils.plugins import Plugins

_path = Path(__file__).absolute().parent

plugins: Plugins = Plugins()


class Settings(BaseSettings):
    class Config:
        env_prefix = "CO2_"
        env_file = ".env"
        env_file_encoding = "utf-8"

    PATH: Path = _path

    APP_PATH: Path = typer.get_app_dir(app_name="co2", force_posix=True)

    LOGORU_FORMAT: str = "<green>{time:YYYY-MM-DD at HH:mm:ss}</green> <level>{level}</level> - {message}"
    LOGURU_LEVEL: str = "DEBUG"

    # Method
    @classmethod
    @model_validator(mode="before")
    def prevent_none(cls, fields):
        for k, v in fields.items():
            if v is None:
                raise ValueError(f"The fields '{k}' must not be None")
        return fields


settings: Settings = Settings()
