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
        return {
            name: importlib.import_module(name)
            for finder, name, ispkg in pkgutil.iter_modules()
            if name.startswith("co2_")
        }
