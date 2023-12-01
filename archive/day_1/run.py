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
    total = 0
    for line in data:
        re_digits_pattern = "|".join(digits)
        nums = re.findall(f"\d|{re_digits_pattern}", line, overlapped=True)
        nums = "".join([i if i not in digits else str(digits.index(i)+1) for i in nums])
        total+=int(nums[0]+nums[-1])
    return total

SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_1.t')
    eout = 281
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_1.m')
    print("main: ", mout)
