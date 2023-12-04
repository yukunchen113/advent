import requests
from pathlib import Path
import sys
import os
import re

DAYS_FOLDER = "2023"

def get_latest_day():
    return int(re.findall("\d+", [i for i in sorted(os.listdir(DAYS_FOLDER))][-1])[-1])

def getfilepaths(day: int) -> dict[str, str]:
    basedir = os.path.join(DAYS_FOLDER, f"day_{day}")
    return {
        "basedir": basedir,
        "code": os.path.join(basedir, "code.py"),
        "mdata": os.path.join(basedir, "data.m"),
        "tdata": os.path.join(basedir, "data.t"),
        "retro": os.path.join(basedir, "retro.md"),
    }

def create_day_files(day: int) -> None:
    files = getfilepaths(day)
    code = files["code"]
    mdata = files["mdata"]
    tdata = files["tdata"]
    retro = files["retro"]
    
    os.makedirs(files["basedir"], exist_ok=True)
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
from advent import mark
from advent.tools.map import convert_to_complex

def parse_input(data_file):
    with open(data_file) as f:
        lines = [i.replace("\\n", "") for i in f.readlines()]
    return lines

@mark.solution(test=None)
def pt1(data_file):
    data = parse_input(data_file)
""")