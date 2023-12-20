# Advent of Code
Personal library for Advent of Code.

`advent/` contains a library of functionality, and doubles as a callable module.

## Setup

Create a file in the main directory called `advent_secrets.py` and then create variables following the instructions [from](https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py):
- SESSION = (session retrieved following instructions above)
- USERAGENT = (your github path to the create.py file) followed by your email.
	- eg. 'https://github.com/yukunchen113/advent/blob/main/advent/create.py by yukunchen113@gmail.com'

## Creating a New Day
- By default, dates are created under the base folder defined in advent/create - DAYS_FOLDER
	- you can specify a specific date with the `--year <year>` command
		- for example `python -m advent --year 2021` will run the latest AoC date in the 2021 repo
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
- running a day will run through your solutions and will pull your puzzle input after the question is released, if not done before.

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

@mark.solution(test=None)
def pt2(data_file):
	pass

# will run through data.t input
@mark.solution(test=123)
def pt2(data_file):
	pass

# will not raise assertion error with test input, good for debugging.
@mark.solution(test=123)
def pt2(data_file):
	return None # or no return statement

```