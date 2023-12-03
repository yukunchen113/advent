import requests
from pathlib import Path
import sys
import os

ARCHIVE_FOLDER = "archive"


def getfilenames(day):
    return {
        "code": f"run.py",
        "mdata": f"data_{day}.m",
        "tdata": f"data_{day}.t",
        "retro": f"day_{day}.retro",
    }


def move_files(day):
    for file in getfilenames(day-1).values():
        if os.path.exists(file):
            basepath = os.path.join(ARCHIVE_FOLDER, f"day_{day-1}")
            os.makedirs(basepath,exist_ok=True)
            dest= os.path.join(basepath, file)
            if not os.path.exists(dest):
                os.rename(file, dest)


def create_day_files(day):
    files = getfilenames(day)
    code = files["code"]
    mdata = files["mdata"]
    tdata = files["tdata"]
    retro = files["retro"]

    # test data file:
    if not os.path.exists(tdata):
        Path(tdata).touch()

    # main data file:
    if not os.path.exists(mdata):
        Path(mdata).touch()
    
    # main data file:
    if not os.path.exists(retro):
        Path(retro).touch()

    # Starter Code:
    if os.path.exists(code):
        print(f"{code} already exists... skipping")
        return
    else:
        with open(code, 'w') as f:
            f.write(
                f"""import os
from collections import defaultdict
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
import library

def parse_input(data_file):
    with open(data_file) as f:
        lines = [i.replace("\\n", "") for i in f.readlines()]
    return lines

def main(data_file):
    data = parse_input(data_file)

if __name__ == "__main__":
    tout = main('{tdata}')
    eout = 
    assert tout == eout, tout
    print("Test Success")
    mout = main('{mdata}')
    print("main: ", mout)
""")


day = int(sys.argv[1])
move_files(day)
create_day_files(day)
