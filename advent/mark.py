"""
This file contains functionality to mark a particular function to run.
"""
import os
from typing import Any, Callable, Optional
import importlib
from advent.create import getfilepaths, DAYS_FOLDER
from inspect import getmembers

class Solution:
	def __init__(self, func, test: Any = None):
		self.func = func
		self.test = test
	def __call__(self, basepath):
		if self.test is not None:
			tout = self.func(os.path.join(basepath, 'data.t'))
			if tout is None: return
			if tout != self.test:
				print(f"Wrong Test Answer: {tout}")
				exit()
			print("Test Success")
		mout = self.func(os.path.join(basepath, 'data.m'))
		print("main: ", mout)
		

def solution(test: Any = None) -> Callable:
	"""
	To be used as function decorator.
	
	Will register function as a solution to problem and run it with the testing specified.
	"""
	if isinstance(test, Callable):
		return Solution(test, None)
	def wrapper(func):
		return Solution(func, test)
	return wrapper

def run_solutions(day: int, year: Optional[str] = None):
	if year is None:
		year = DAYS_FOLDER
	code = importlib.import_module(f'{year}.day_{day}.code')
	for name, solution in getmembers(code, lambda x: isinstance(x, Solution)):
		print(f"\033[95m{name}\033[0m")
		solution(getfilepaths(day, year)["basedir"])