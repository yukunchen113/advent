import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

# @mark.solution(test=374)
def pt1(data_file):
    data = [list(i.strip()) for i in open(data_file).readlines()]
    # expand rows & cols
    ndata = []
    for row in data:
        if all([i == "." for i in row]):
            ndata.append(row)
        ndata.append(row)
    data = ndata
    
    ndata = []
    for ridx,row in enumerate(data):
        nrow = []
        for cidx, ele in enumerate(row):
            if all([i == "." for i in np.array(data)[:, cidx]]):
                nrow.append(ele)
            nrow.append(ele)
        ndata.append(nrow)
    data = ndata    
            
    # get shortest paths for each point
    map = convert_to_complex(data)
    pairs = defaultdict(dict)
    for point in [c for c,v in map.items() if v == "#"]:
        nodes = [point]
        visited = set()
        level = 0
        while nodes:
            nnodes = []
            for node in nodes:
                if node not in map or node in visited:
                    continue
                visited.add(node)
                if map[node] == "#" and not node in pairs:
                    pairs[point][node] = level
                for dir in [1,-1j,-1,1j]:
                    nnodes.append(node+dir)
            nodes = nnodes
            level += 1
    return sum([sum(i.values()) for i in pairs.values()])


@mark.solution(test=None)
def pt2(data_file):
    times_larger = -1+1000000
    data = [list(i.strip()) for i in open(data_file).readlines()]
    # expand rows & cols
    erows = []
    for ridx,row in enumerate(data):
        if all([i == "." for i in row]):
            erows.append(ridx)
    ecols = []
    for cidx, _ in enumerate(row):
        if all([i == "." for i in np.array(data)[:, cidx]]):
            ecols.append(cidx)
    
    data = convert_to_complex(data)
    data = {k:v for k,v in data.items() if v == "#"}
    ndata = {}
    for point, val in data.items():
        npoint = point+(times_larger*len([i for i in erows if i < point.real]))+(1j*times_larger*len([i for i in ecols if i < point.imag]))
        ndata[npoint] = val
    data = ndata
    
    points = list(data.keys())
    total = 0
    for idx,p1 in enumerate(points[:-1]):
        for p2 in points[idx+1:]:
            total += int(abs((p2-p1).real) + abs((p2-p1).imag))
    return total