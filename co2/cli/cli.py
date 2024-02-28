import importlib
import pkgutil

import typer

discovered_plugins = {
    name: importlib.import_module(name)
    for finder, name, ispkg in pkgutil.iter_modules()
    if name.startswith("co2_")
}

cli = typer.Typer(no_args_is_help=True)

for name, plugin in discovered_plugins.items():
    cli.add_typer(plugin.cli, name=name.replace("co2_", ""))


@cli.command()
def hello():
    print("Hello")


@cli.command()
def goodbye():
    print("Goodbye")
