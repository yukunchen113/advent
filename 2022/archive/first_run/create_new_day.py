import requests
from pathlib import Path
import sys
import os

ARCHIVE_FOLDER = "archive"


def getfilenames(day):
    return {
        "code": f"day_{day}.py",
        "mdata": f"data_{day}.m",
        "tdata": f"data_{day}.t",
    }


def move_files(day):
    for file in getfilenames(day-1).values():
        if os.path.exists(file):
            os.rename(file, os.path.join(ARCHIVE_FOLDER, file))


def create_day_files(day):
    files = getfilenames(day)
    code = files["code"]
    mdata = files["mdata"]
    tdata = files["tdata"]

    # test data file:
    if not os.path.exists(tdata):
        Path(tdata).touch()

    # main data file:
    if not os.path.exists(mdata):
        Path(mdata).touch()

    # Starter Code:
    if os.path.exists(code):
        print(f"{code} already exists... skipping")
        return
    else:
        with open(code, 'w') as f:
            f.write(
                f"""import os
from collections import defaultdict

def parse_input(data_file):
    with open(data_file) as f:
        lines = f.readlines()
    return lines

def main(data_file):
    data = parse_input(data_file)

SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('{tdata}')
    eout = 
    assert tout == eout, tout
    print("Test Success")
    mout = main('{mdata}')
    print("main: ", mout)
""")


day = int(sys.argv[1])
create_day_files(day)
move_files(day)
