#!/usr/bin/env python
import urllib.request, os, zipfile, shutil

working_directory = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
newest_ver = str(urllib.request.urlopen("https://raw.githubusercontent.com/alan67160/ITP3915Assignment/master/VERSION").read()).strip("b\'")
current_ver = open(working_directory + "/VERSION", "r").read()
if not (current_ver == newest_ver):
    print(f"The current application version is {current_ver}. (newest:{newest_ver})")
    urllib.request.urlretrieve("https://github.com/alan67160/ITP3915Assignment/archive/refs/heads/master.zip", working_directory + "/update.zip")
    with zipfile.ZipFile(working_directory + "/update.zip", 'r') as update_zip:
        update_zip.extractall(working_directory + "/tmp")
    os.remove(working_directory + "/update.zip")
    for file in os.listdir(working_directory + "/tmp/ITP3915Assignment-master"):
        try:
            shutil.move(os.path.join(working_directory + "/tmp/ITP3915Assignment-master", file), os.path.join(working_directory, file))
        except shutil.Error:
            pass
    shutil.rmtree(working_directory + "/tmp")