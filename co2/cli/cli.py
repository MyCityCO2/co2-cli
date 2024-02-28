import typer

from co2 import __version__
from co2.cli.plugins import cli as plugins_cli
from co2.const import Plugins

cli = typer.Typer(no_args_is_help=True)

plugins = Plugins()

for name, plugin in plugins.plugins:
    cli.add_typer(plugin.cli, name=name)

cli.add_typer(plugins_cli, name="plugins")


@cli.command()
def version() -> None:
    print(f"Current version is {__version__}")
