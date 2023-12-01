import os
from collections import defaultdict
import regex as re
from pprint import pprint

def parse_input(data_file):
    with open(data_file) as f:
        lines = [i.replace("\n", "") for i in f.readlines()]
    return lines

def main(data_file):
    data = parse_input(data_file)

SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_2.t')
    eout = 
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_2.m')
    print("main: ", mout)


import os
from collections import defaultdict
import regex as re
from pprint import pprint

def parse_input(data_file):
    with open(data_file) as f:
        lines = [i.replace("\n", "") for i in f.readlines()]
    return lines

def main(data_file):
    data = parse_input(data_file)
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in data:
        re_digits_pattern = "|".join(digits)
        digits = re.findall(f"\d|{re_digits_pattern}", line)
        print(digits)

SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_2.t')
    eout = 281
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_2.m')
    print("main: ", mout)
