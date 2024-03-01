import typer

from co2.utils.plugins import Plugins

cli = typer.Typer(no_args_is_help=True)

plugins = Plugins()


@cli.command()
def list() -> None:
    print(f"There are {len(plugins.plugins)} installed plugins:")
    for name, plugin in plugins.plugins:
        print(f"- {name} | {plugin.__version__}")
