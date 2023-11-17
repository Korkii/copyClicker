import os
import random
from pathlib import Path
import string


def random_string(min_length=5, max_length=10):
    """
    Get a random string
    Args:
        min_length: Minimal length of string
        max_length: Maximal length of string
    Returns:
        Random string of ascii characters
    """
    length = random.randint(min_length, max_length)
    return ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for _ in range(length)
    )


def generate_folder_line(baseDir: str, averNumofFolders: int, sigmaFolders: int, maxDepth: int, counter=0):
    Folders = []
    if counter == maxDepth:
        return []

    for root, Folders, files in os.walk(str(baseDir)):
        for _ in range(int(random.gauss(averNumofFolders, sigmaFolders))):
            currFolder = random_string()
            p = Path(root) / currFolder
            p.mkdir(exist_ok=True)
            Folders.append(p)
            generate_folder_line(p, averNumofFolders,
                                 sigmaFolders, maxDepth, counter+1)
        depth = os.path.relpath(root, str(baseDir)).count(os.sep)
        if maxDepth and depth >= maxDepth - 1:
            del Folders[:]

    alldirs = list(set(Folders))
    return alldirs


# Use for this project: generate_folder_line("RandomFolders", 10, 10, 4)
