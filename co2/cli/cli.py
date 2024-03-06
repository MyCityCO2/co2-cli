import sys

import typer
from loguru import logger

from co2 import __version__
from co2.cli.plugins import cli as plugins_cli
from co2.const import settings
from co2.utils.plugins import Plugins

logger.remove(0)
logger.level("FTRACE", no=3, color="<blue>")

logger.add(
    sys.stdout,
    enqueue=True,
    backtrace=True,
    diagnose=True,
    colorize=True,
    format=settings.LOGORU_FORMAT,
    level=settings.LOGURU_LEVEL,
)


cli = typer.Typer(no_args_is_help=True)

plugins = Plugins()

for name, plugin in plugins.plugins:
    cli.add_typer(plugin.cli, name=name)

cli.add_typer(plugins_cli, name="plugins")


@cli.command()
def version() -> None:
    print(f"Current version is {__version__}")
