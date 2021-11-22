#!/usr/bin/env python
import os
import sys
import shutil
import zipfile
import urllib.request
from app.main import main
from app.util import dprint

# Environment variables
working_directory = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
update_url = "https://raw.githubusercontent.com/alan67160/ITP3915Assignment/master/VERSION"
repository_url = "https://github.com/alan67160/ITP3915Assignment"
file_list = ("/app/__init__.py",
             "/app/config.py",
             "/app/environment_variable.py",
             "/app/main.py",
             "/app/util.py",
             "/data/borrowed.txt",
             "/data/borrowers.txt",
             "/data/items.txt",
             "/config.ini",
             "/VERSION")

# update
def update():
    try:
        newest_ver = str(str(urllib.request.urlopen(update_url).read()).strip("b\'"))
        current_ver = open(working_directory + "/VERSION", "r").read()
        print(f"The current application version is {current_ver}. (newest:{newest_ver})")
        if not (current_ver == newest_ver):
            print("[Note] Update functions are still in the experimental stage!")
            print(f"[Note] If you want you can manually update, by going to {repository_url}")
            update_ask = input("Newer version found! Do you want to update the application? [Y/n]").lower()
            if (update_ask == "y") or (update_ask == "yes"):
                print("Attempting to update...")
                urllib.request.urlretrieve(repository_url + "/archive/refs/heads/master.zip",
                                           working_directory + "/update.zip")
                with zipfile.ZipFile(working_directory + "/update.zip", 'r') as update_zip:
                    update_zip.extractall(working_directory + "/tmp")
                os.remove(working_directory + "/update.zip")
                for file in os.listdir(working_directory + "/tmp/ITP3915Assignment-master"):
                    try:
                        shutil.move(os.path.join(working_directory + "/tmp/ITP3915Assignment-master", file),
                                    os.path.join(working_directory, file))
                    except:
                        pass
                shutil.rmtree(working_directory + "/tmp")
                print("update completed!")
            else:
                print("update skipped!")
    except:
        print("\033[93m[WARN] An unexpected error occurred while trying to check the update.\n"
              "Please contact the developer!")


def check_python3():
    try:
        if not ((sys.version_info.major == 3) and (sys.version_info.minor > 6)):
            print("This application required python 3 to run.\nPlease upgrade your python!")
            exit(1)
    except Exception:
        print("An unexpected error occurred while trying to check the python version.\nPlease contact the developer!")
        exit(1)


def check_file():
    dprint("Checking file")
    for i in file_list:
        if not os.path.isfile(working_directory + i):
            print("missing file detected")
            print(f"File path: {working_directory + i}")
            exit(1)
        else:
            dprint(f"File path: {working_directory + i} [detected]", "ok")
    dprint("All file are detected!", "ok")


if __name__ == "__main__":
    check_file()
    check_python3()
    update()
    main()
