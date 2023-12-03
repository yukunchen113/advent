import os
from collections import defaultdict
import regex as re
from pprint import pprint
import functools
from operator import mul
import numpy as np


def parse_input(data_file):
    with open(data_file) as f:
        lines = [i.replace("\n", "") for i in f.readlines()]
    return lines

caps = {"red":12, "green":13, "blue":14}

def main(data_file):
    data = parse_input(data_file)
    out = 0
    for idx,line in enumerate(data,1):
        nums = re.findall(r"(?:(\d+) (blue|red|green))", line)
        min_game = {"green":-float("inf"),"red":-float("inf"),"blue":-float("inf")}
        for num,color in nums:
            min_game[color] = max(int(num), min_game[color], 0)
        prod = 1
        for i in min_game.values():
            prod*=i
        out += prod
    return out
        

def new_main(data_file):
    data = parse_input(data_file)
    out = 0
    for idx,line in enumerate(data,1):
        nums = re.findall(r"(\d+) (b|r|g)", line)
        min_game = {"g":0,"r":0,"b":0}
        for num,color in nums:
            min_game[color] = max(int(num), min_game[color], 0)
        out+=functools.reduce(mul, min_game.values(), 1)
    return out

def np_main(data_file):
    data = parse_input(data_file)
    out = 0
    for idx,line in enumerate(data,1):
        nums = re.findall(r"(\d+) (blue|red|green)", line)
        min_game = {"green":[],"red":[],"blue":[]}
        for num,color in nums:
            min_game[color].append(int(num))
        game = np.max(min_game.values(),axis=1)
        out+=np.prod(game)
    return out

SHOW_MAIN = 0
if __name__ == "__main__":
    tout = new_main('data_2.t')
    eout = 2286
    assert tout == eout, tout
    print("Test Success")
    mout = new_main('data_2.m')
    print("main: ", mout)
