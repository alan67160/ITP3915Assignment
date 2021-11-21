from .debug import dprint
from .config import Config as config
from .environment_variable import Variable as ve
from functools import cache

class Items:
    @cache
    def __init__(self):
        if config.storage.user.value == "txt":
            dprint("TXT mode")
            global ITEMS
            raw_items, sub_items, ITEMS = str(), tuple(), list()
            dprint(f"Loading {ve.working_directory}/data/items.txt")
            with open(ve.working_directory + "/data/items.txt", "r") as file:
                for read in file:
                    if not (read.startswith("# ") or (read == "\n")):
                        raw_items += read
                raw_items = raw_items.split("\n")
                dprint(f"ItemName                                   | ItemBrand       | ItemQuantity")
                for runtime in range(len(raw_items)):
                    sub_items += tuple(raw_items[runtime].split(", "))
                    if len(sub_items) == 3:
                        dprint(f"{sub_items[0]:<42} | {sub_items[1]:<15} | {sub_items[2]}")
                        ITEMS.append(tuple(sub_items))
                        sub_items = ()
                ITEMS = tuple(ITEMS)
            dprint("Base item list Loaded!", "ok")

    def get(self):
        return ITEMS