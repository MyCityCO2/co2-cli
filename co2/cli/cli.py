import importlib
import pkgutil

import typer

from co2.cli.plugins import plugins

from co2 import __version__

discovered_plugins = {
    name: importlib.import_module(name)
    for finder, name, ispkg in pkgutil.iter_modules()
    if name.startswith("co2_")
}

cli = typer.Typer(no_args_is_help=True)

for name, plugin in discovered_plugins.items():
    cli.add_typer(plugin.cli, name=name.replace("co2_", ""))

cli.add_typer(plugins, name="plugins")


@cli.command()
def version():
    print(f"Current version is {__version__}")
