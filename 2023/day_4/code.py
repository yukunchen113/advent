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

@mark.solution(test=13)
def pt1(data_file):
    data = parse_input(data_file)
    total = 0
    for line in data:
        enums, ynums = line.split(":")[1].split("|")
        enums = [int(num) for num in re.findall(r"\d+", enums)]
        ynums = [int(num) for num in re.findall(r"\d+", ynums) if int(num) in enums]
        if ynums:
            total += 2**(len(ynums)-1)
    return total
            
@mark.solution(test=30)
def pt2_uniqueness_assumption(data_file):
    data = parse_input(data_file)
    cards = {i+1:1 for i in range(len(data))}
    for idx,line in enumerate(data, 1):
        enums, ynums = line.split(":")[1].split("|")
        for i in range(len(set(ynums.split()) & set(enums.split()))):
            cards[idx+i+1]+=cards[idx]
    return sum(cards.values())

def pt2(data_file):
    data = parse_input(data_file)
    cards = { i+1:1 for i in range(len(data))}
    for idx,line in enumerate(data, 1):
        enums, ynums = line.split(":")[1].split("|")
        enums = [int(num) for num in re.findall(r"\d+", enums)]
        ynums = [int(num) for num in re.findall(r"\d+", ynums) if int(num) in enums]
        for i in range(len(ynums)):
            cards[idx+i+1]+=cards[idx]
    return sum(cards.values())