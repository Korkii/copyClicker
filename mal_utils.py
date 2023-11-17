import os
from glob import iglob
from random import choice
import shutil


def dupe(dest_folder: str, file: str):
    shutil.copy(file, dest_folder + os.sep + "copied")
    print(dest_folder + os.sep + "copied.py")


def get_random_dir(root: str):

    if [f for f in os.listdir(root) if os.path.isdir(root+'\\'+f)] == []:
        print("returned")
        return root
    currDir = []
    for f in os.listdir(root):
        if os.path.isdir(root+'\\'+f):
            currDir.append(root+'\\'+f)
    return get_random_dir(choice(currDir))
