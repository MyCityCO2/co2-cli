from pathlib import Path

import typer
from pydantic import model_validator
from pydantic_settings import BaseSettings

_path = Path(__file__).absolute().parent


class Settings(BaseSettings):
    class Config:
        env_prefix = "CO2_"
        env_file = ".env"
        env_file_encoding = "utf-8"

    APP_PATH: Path = typer.get_app_dir(app_name="co2", force_posix=True)

    LOGORU_FORMAT: str = "<green>{time:YYYY-MM-DD at HH:mm:ss}</green> <level>{level}</level> - {message}"
    LOGURU_LEVEL: str = "DEBUG"

    COA_SET_NAMING: str = "coa-{name}.csv"
    COA_SET_WILDCARD: str = "coa-*.csv"
    COA_SET_REGEX: str = r"(?<=coa-).+?(?=.csv)"

    ACCOUNT_SET_NAMING: str = "account-{district}.csv"
    ACCOUNT_SET_WILDCARD: str = "account-*.csv"
    ACCOUNT_SET_REGEX: str = r"(?<=account-).+?(?=.csv)"

    CARBON_FILE_PATH: str = (
        "carbon_factor.csv"  # This file is there to create all carbon.factor in Odoo...
    )

    # Method
    @classmethod
    @model_validator(mode="before")
    def prevent_none(cls, fields):
        for k, v in fields.items():
            if v is None:
                raise ValueError(f"The fields '{k}' must not be None")
        return fields


settings: Settings = Settings()
