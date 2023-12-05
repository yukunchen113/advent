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
    mapping = []
    for line in lines:
        if line.startswith("seeds: "):
            seeds = [int(i) for i in re.findall("\d+", line)]
        elif ":" in line:
            mapping.append([])
        elif line:
            mapping[-1].append([int(i) for i in line.split()])    
    return seeds, mapping

def get_next_mapping(mapping, seed):
    for des,sou,ran in mapping:
        if sou<=seed<(sou+ran):
            return seed-sou+des
    return seed

#@mark.solution(test=35)
def pt1(data_file):
    seeds, mappings = parse_input(data_file)
    minitem = float("inf")
    for seed in seeds:
        item = seed
        for mapping in mappings:
            item = get_next_mapping(mapping, item)
        minitem = min(minitem, item)
    return minitem

@mark.solution(test=46)
def pt2(data_file):
    seeds, mappings = parse_input(data_file)
    seeds = np.cumsum(np.reshape(seeds,(-1,2)), axis=1).tolist()
    minitem = float("inf")
    for seed in seeds:
        item = seed
        for mapping in mappings:
            item = get_next_mapping(mapping, item)
        minitem = min(minitem, item)
    return minitem