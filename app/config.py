try:
    from configparser import ConfigParser
except ImportError:
    # Legacy ConfigParser support
    from ConfigParser import ConfigParser
from .environment_variable import Variable as ve
from enum import Enum
config = ConfigParser()
config.read(ve.working_directory.value + '/config.ini')

class Config(Enum):
    class storage(Enum):
        user = str(config.get("storage", "user"))
        item = str(config.get("storage", "item"))
        borrowed = str(config.get("storage", "borrowed"))
    debug = not not (config.get("settings", "debug").lower() == "true")

