from tap import tapify
from typing import Optional
import os
from advent.create import getfilepaths, create_day_files, get_latest_day, pull_data
from advent.mark import run_solutions

def main(day: Optional[int] = None, next:bool = False, year: Optional[str] = None):
	"""
	Main that will perform required actions for specified day
	"""
	if year is not None:
		print(f"Running Specified Year {year}")
	if day is None:
		# get latest day
		day = get_latest_day(year=year)+next
	if not 0 < day <= 25:
		print(f"Invalid Day {day}")
		exit()
	if os.path.exists(getfilepaths(day, year=year)["basedir"]):
		print(f"Running Day {day}")
		pull_data(day=day, year=year)
		run_solutions(day=day, year=year)
	else:
		print(f"Creating Day {day}")
		create_day_files(day, year=year)
	
	

if __name__ == "__main__":
	tapify(main)