from enum import Enum
import configparser
from .environment_variable import Variable as ev
config = configparser.ConfigParser()
config.read(ev.working_directory.value + '/config.ini')


class Config:
    try:
        debug = config.getboolean("settings", "debug")
        user = config.get("storage", "user")
        item = config.get("storage", "item")
        borrowed = config.get("storage", "borrowed")
        borrow_limit = config.getint("settings", "borrow_limit")
    except Exception as e:
        print("An unexpected error occurred while trying to load config.ini.\nPlease contact the developer!")
        print(f"Error: {e}")
        exit(1)


