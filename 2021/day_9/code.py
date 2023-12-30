import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=15)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    data = convert_to_complex(data)
    total = 0
    for point in data:
        if data[point] < min(data.get(point+dir, "99") for dir in [1,-1,-1j,1j]):
            total += int(data[point])+1
    return total

@mark.solution(test=1134)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    data = convert_to_complex(data)
    basins = []
    for point in data:
        if int(data[point]) < min(int(data.get(point+dir, 10))
            for dir in [1,-1,-1j,1j]):
                nodes = [point]
                seen = set()
                while nodes:
                    node = nodes.pop()
                    if node not in data or data[node] == "9" or node in seen:
                        continue
                    seen.add(node)
                    for dir in [1,-1,-1j,1j]:
                        if int(data.get(node+dir, -1)) > int(data[node]):
                            nodes.append(node+dir)
                basins.append(len(seen))
    return np.prod(sorted(basins)[-3:])