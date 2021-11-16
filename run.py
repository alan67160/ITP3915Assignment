#!/usr/bin/env python
import urllib.request, os, zipfile, shutil, sys
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

# Environment variables
working_directory = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
update_url = "https://raw.githubusercontent.com/alan67160/ITP3915Assignment/master/VERSION"
repository_url = "https://github.com/alan67160/ITP3915Assignment"
config = ConfigParser()
config.read(working_directory + 'config.ini')
try:
    debug = bool(config.get("settings", "debug"))
except:
    debug = False

def dprint(msg, *type):
    type = str(type).lower() ; color = ""
    if type == "ok": color = "\033[92m"
    if type == "warn": color = "\033[92m"
    if type == "fail": color = "\033[92m"
    if debug: print(f"{color}[DEBUG] {msg}\033[0m")

# update
def update():
    try:
        newest_ver = str(str(urllib.request.urlopen(update_url).read()).strip("b\'"))
        current_ver = open(working_directory + "/VERSION", "r").read()
        print(f"The current application version is {current_ver}. (newest:{newest_ver})")
        if not (current_ver == newest_ver):
            update_ask = input("Newer version found! Do you want to update the application? [Y/n]").lower()
            if (update_ask == "y") or (update_ask == "yes"):
                print("Attempting to update...")
                urllib.request.urlretrieve(repository_url + "/archive/refs/heads/master.zip", working_directory + "/update.zip")
                with zipfile.ZipFile(working_directory + "/update.zip", 'r') as update_zip:
                    update_zip.extractall(working_directory + "/tmp")
                os.remove(working_directory + "/update.zip")
                for file in os.listdir(working_directory + "/tmp/ITP3915Assignment-master"):
                    try:
                        shutil.move(os.path.join(working_directory + "/tmp/ITP3915Assignment-master", file), os.path.join(working_directory, file))
                    except:
                        pass
                shutil.rmtree(working_directory + "/tmp")
                print("update completed!")
            else:
                print("update skipped!")
    except:
        print("\033[93m[WARN] An unexpected error occurred while trying to check the update.\nPlease contact the developer!")

def checkpython3():
    try:
        if not (sys.version_info.major == 3):
            print("This application required python 3 to run.\nPlease upgrade your python!")
            exit(1)
    except:
        print("An unexpected error occurred while trying to check the python version.\nPlease contact the developer!")
        exit(1)

def checkConfig():
    try:
        if not ((config.get("storage", "user") == "txt") or (config.get("storage", "user") == "sqlite")):
            if bool(config.get("settings", "debug")): print("An unexpected error occurred while trying to read the user storage type in config.")
            return False
        if not ((config.get("storage", "item") == "txt") or (config.get("storage", "item") == "sqlite")):
            if bool(config.get("settings", "debug")): print("An unexpected error occurred while trying to read the item storage type in config.")
            return False
        if not ((config.get("settings", "debug") == "True") or (config.get("settings", "debug") == "False")):
            if bool(config.get("settings", "debug")): print("An unexpected error occurred while trying to read the debug mode in config.")
            return False
        return True
    except:
        return False

if __name__ == "__main__":
    checkpython3()
    update()
    if not checkConfig:
        exit(1)
    from app.main import main
    main()
