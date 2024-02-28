import typer
import importlib
import pkgutil


discovered_plugins = {
    name: importlib.import_module(name)
    for finder, name, ispkg in pkgutil.iter_modules()
    if name.startswith("co2_")
}

plugins = typer.Typer(no_args_is_help=True)

@plugins.command()
def list():
    print(f"There are {len(discovered_plugins)} installed plugins:")
    for name, _ in discovered_plugins.items():
        print(f"- {name.replace('co2_', '')}")