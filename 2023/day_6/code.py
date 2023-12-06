import os
from collections import defaultdict
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

def parse_input(data_file):
    with open(data_file) as f:
        lines = [i.replace("\n", "") for i in f.readlines()]
    return lines

@mark.solution(test=288)
def pt1(data_file):
    data = parse_input(data_file)
    times = [int(i) for i in re.findall(r"\d+", data[0].split(":")[1])]
    dists =[int(i) for i in re.findall(r"\d+", data[1].split(":")[1])]
    out = 1
    for time,dist in zip(times,dists):
        wins = 0
        for ht in range(1,time+1):
            wins += ht*(time-ht) > dist
        out *= wins
    return out

@mark.solution(test=71503)
def pt2(data_file):
    data = parse_input(data_file)
    time = int("".join([i for i in re.findall(r"\d+", data[0].split(":")[1])]))
    dist =int("".join([i for i in re.findall(r"\d+", data[1].split(":")[1])]))
    wins = 0
    for ht in range(1,time+1):
        wins += ht*(time-ht) > dist
    return wins