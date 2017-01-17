import glob
import os

# get the current directory to run script on
curDir = os.getcwd()

# testing scandir fucntionality. Will be removed later
with os.scandir(curDir) as list:
    for entry in list:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)
