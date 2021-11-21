from .debug import dprint
from functools import cache
from .config import Config as config
from .environment_variable import Variable as ve

class main:
    @cache
    def __init__(self):
        if config.storage.user == "txt":
            try:
                global user_list
                global user_list_by_name
                sub_user_list, user_list_by_name, user_list = list(), dict(), dict()
                dprint("TXT mode")
                dprint(f"Loading {ve.working_directory}/data/borrowers.txt")
                with open(ve.working_directory + "/data/borrowers.txt", "r") as file_read:
                    for user in file_read:
                        if not (user.startswith("# ") or (user == "\n")):
                            sub_user_list.append(user.rstrip("\n").split(", "))
                dprint(f"No. | Username", "data")
                for runtime in range(len(sub_user_list)):
                    dprint(f"{runtime:<3} | {str(sub_user_list[runtime][0]).lower()}", "data")
                    user_list[runtime] = str(sub_user_list[runtime][0]).lower()
                    user_list_by_name[str(sub_user_list[runtime][0]).lower()] = runtime
                dprint("User list Loaded!", "ok")
            except NameError:
                dprint("\033[91m[WARN] An unexpected error occurred while trying to initialize the user list...")

    def no(self):
        return user_list

    def name(self):
        return user_list_by_name
