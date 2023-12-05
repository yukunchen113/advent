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
    for des, sou, ran in mapping:
        if sou <= seed < (sou + ran):
            return seed - sou + des
    return seed


@mark.solution(test=35)
def pt1(data_file):
    seeds, mappings = parse_input(data_file)
    minitem = float("inf")
    for seed in seeds:
        item = seed
        for mapping in mappings:
            item = get_next_mapping(mapping, item)
        minitem = min(minitem, item)
    return minitem


def get_intersect_ranges(start, end, mapping) -> list[tuple[int, int]]:
    breakpoints = set([start, end + 1])
    for _, sou, ran in mapping:
        if start < sou < end:
            breakpoints.add(sou)
        if start < (sou + ran) < end:
            breakpoints.add(sou + ran)
    breakpoints = sorted(list(breakpoints))
    ranges = []
    for idx, bp in enumerate(breakpoints[:-1]):
        ranges.append((bp, breakpoints[idx + 1] - 1))
    return ranges


@mark.solution(test=46)
def pt2(data_file):
    seeds, mappings = parse_input(data_file)
    rseeds = np.reshape(seeds, (-1, 2))
    rseeds[:, 1] -= 1
    rseeds = np.cumsum(rseeds, axis=1).tolist()  # inclusive range of values
    minitem = float("inf")
    ritems = rseeds
    for mapping in mappings:
        nitems = []
        for si, ei in ritems:
            ranges = get_intersect_ranges(si, ei, mapping)
            ranges = [
                (get_next_mapping(mapping, s), get_next_mapping(mapping, e))
                for s, e in ranges
            ]
            nitems += ranges
        ritems = nitems
    minitem = min([i for j in ritems for i in j])
    return minitem
