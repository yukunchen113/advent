from tap import tapify
import importlib
from typing import Optional
import os
from datetime import datetime
from advent.create import getfilepaths, create_day_files, get_latest_day
from advent.mark import run_solutions

def main(day: Optional[int] = None, next:bool = False):
	"""
	Main that will perform required actions for specified day
	"""
	if day is None:
		# get latest day
		day = get_latest_day()+next
	if not 0 < day <= 25:
		print(f"Invalid Day {day}")
	if os.path.exists(getfilepaths(day)["basedir"]):
		print(f"Running Day {day}")
		run_solutions(day=day)
	else:
		print(f"Creating Day {day}")
		create_day_files(day)
	
	

if __name__ == "__main__":
	tapify(main)