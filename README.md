# Advent of Code
Personal library for Advent of Code.

`advent/` contains a library of functionality, and doubles as a callable module.

## Creating a New Day
- Dates are created under the base folder defined in advent/create - DAYS_FOLDER
- to create a new day you can run the following commands:
	- `python -m advent --day X` where `X` is a int for the AOC day.
		- a new day is created if it doesn't currently exist
	- `python -m advent --next` will create the newest date.
- creating a day will create the following files:
	- `code.py`: where the main code exists.
	- `data.m`: a file containing personal puzzle input
	- `data.t`: a file containing provided test input
	- `retro.md`: a file containing retrospective of performance after day. 


## Running Days
- to run a particular day you can run the following commands:
	- `python -m advent`, which will run through all the `Solution`s in the latest day.
	- `python -m advent --day X` where `X` is a int for the AOC day.
		- if the day currently exists, it will run through all the `Solution`s in that day

## Creating Solutions
- `Solution`s are any function that have the `advent.mark.solution` decorator. 
	- you can specify an additional test case which will run through data using the `data.t` file and validate it.
	- if a test case is not specified, or None, the main data will be run directly.

```python
from advent import mark

# will run main directly
@mark.solution
def pt1(data_file): # function needs to accept data_file as parameter, which is a string containing location of datafile.
	pass

# will run through data.t input
@mark.solution(test=123)
def pt2(data_file):
	pass

```