import requests
from pathlib import Path
import sys
import os
import re
from datetime import datetime
from typing import Optional
from dateutil.tz import gettz
import subprocess
from advent_secrets import USERAGENT, SESSION

DAYS_FOLDER = "2023"

def pull_data(day:int, year: Optional[str] = None):
    # if already pulled or date hasn't started, pull
    if year is None:
        year = DAYS_FOLDER
    fpaths = getfilepaths(day, year)
    if datetime.now(tz=gettz("America/New_York")) < datetime(int(year),12,day,0,0,0,0, tzinfo=gettz("America/New_York")):
        return
    if os.stat(fpaths["mdata"]).st_size > 0:
        return
    cmd = f'curl https://adventofcode.com/{year}/day/{day}/input --cookie "session={SESSION}" -A \'{USERAGENT}\''
    output = subprocess.check_output(cmd, shell=True)
    with open(fpaths["mdata"], "w") as file:
        file.write(output.decode('utf-8'))

def get_latest_day(year: Optional[str] = None) -> int:
    if year is None:
        year = DAYS_FOLDER
    os.makedirs(year, exist_ok=True)
    days = [re.findall(r"\d+", i) for i in os.listdir(year)]
    if not days:
        return 1
    return sorted([int(day[0]) for day in days if day])[-1]

def getfilepaths(day: int, year: Optional[str] = None) -> dict[str, str]:
    if year is None:
        year = DAYS_FOLDER
    basedir = os.path.join(year, f"day_{day}")
    return {
        "basedir": basedir,
        "code": os.path.join(basedir, "code.py"),
        "mdata": os.path.join(basedir, "data.m"),
        "tdata": os.path.join(basedir, "data.t"),
        "retro": os.path.join(basedir, "retro.md"),
    }

def create_day_files(day: int, year: Optional[str] = None) -> None:
    files = getfilepaths(day, year)
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
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=None)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
""")