#!/usr/bin/env python
import urllib.request, os, zipfile, shutil


# environment variables
working_directory = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
update_url = "https://raw.githubusercontent.com/alan67160/ITP3915Assignment/master/VERSION"
repository_url = "https://github.com/alan67160/ITP3915Assignment"


# update
def update():
    newest_ver = str(urllib.request.urlopen(update_url).read()).strip("b\'")
    current_ver = open(working_directory + "/VERSION", "r").read()
    if not (current_ver == newest_ver):
        print(f"The current application version is {current_ver}. (newest:{newest_ver})")
        print("Newer version found! Attempting to update...")
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

def main():
    from app import main