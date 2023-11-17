import os
from glob import iglob
from random import choice


def get_random_dir(root: str):

    if [f for f in os.listdir(root) if os.path.isdir(root+'\\'+f)] == []:
        print("returned")
        return root
    currDir = []
    for f in os.listdir(root):
        if os.path.isdir(root+'\\'+f):
            currDir.append(root+'\\'+f)
            print(f)
    return get_random_dir(choice(currDir))
