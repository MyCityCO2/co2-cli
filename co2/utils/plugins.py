import importlib
import pkgutil


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Plugins:
    def __init__(self, *args, **kwargs):
        self.plugins = self._get_plugins()

    def _get_plugins(self):
        plugins_dict = {
            name: importlib.import_module(name)
            for finder, name, ispkg in pkgutil.iter_modules()
            if name.startswith("co2_")
        }
        plugins = []
        for name, plugin in plugins_dict.items():
            if plugin.__dict__.get("__co2__"):
                plugins.append((name, plugin))

        return plugins
