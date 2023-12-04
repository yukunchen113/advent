import os
from collections import defaultdict
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent.tools.map import convert_to_complex
from advent import mark

def parse_input(data_file):
    with open(data_file) as f:
        lines = [i.replace("\n", "") for i in f.readlines()]
    return lines

def main(data_file):
    data = parse_input(data_file)
    indices2num = {}
    for idx, line in enumerate(data):
        outs = [re.search("\d+", line)]
        if not outs[-1]: continue
        while re.search("\d+", line, pos=outs[-1].end()+1):
            outs.append(re.search("\d+", line, pos=outs[-1].end()+1))
        for out in outs:
            num_jdx = range(out.start(), out.end())
            num = line[out.start():out.end()]
            for j in num_jdx:
                indices2num[(idx, j)] = [(idx,out.start()), int(num)]
    total = 0
    for idx, line in enumerate(data):
        for jdx, symbol in enumerate(line):
            if symbol in ["*"]:
                seen = {}
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if (idx+i,jdx+j) in indices2num:
                            a, b = indices2num[(idx+i,jdx+j)]
                            seen[a] = b
                if len(seen) ==2:
                    a,b = seen.values()
                    total += a*b
    return total
        
        
def new_main(data_file):
    data = parse_input(data_file)
    indices2num = {}
    for idx, line in enumerate(data):
        for nmatch in re.finditer("\d+", line):
            for j in range(nmatch.start(), nmatch.end()):
                indices2num[(idx, j)] = {(idx,nmatch.start()): int(nmatch.group(0))}

    total = 0
    for idx, line in enumerate(data):
        for jdx, symbol in enumerate(line):
            if symbol in ["*"]:
                seen = {}
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if (idx+i,jdx+j) in indices2num:
                            seen.update(indices2num[(idx+i,jdx+j)])
                if len(seen) == 2:
                    a,b = seen.values()
                    total += a*b
    return total

@mark.solution(4361)
def new_main_2_pt1(data_file):
    data = parse_input(data_file)
    dcomp = convert_to_complex(data)
    seen = []
    for idx, line in enumerate(data):
        for num in re.finditer("\d+",line):
            coords = {complex(idx+i,j) for j in range(num.start()-1, num.end()+1) for i in [-1,0,1]}
            if any(dcomp.get(coord, ".") not in [str(i) for i in range(10)] +["."] for coord in coords):
                seen.append(int(num.group()))
    return sum(seen)
    
@mark.solution(467835)
def new_main_2(data_file):
    data = parse_input(data_file)
    dcomp = convert_to_complex(data)
    seen = defaultdict(list)
    for idx, line in enumerate(data):
        for num in re.finditer("\d+",line):
            coords = {complex(idx+i,j) for j in range(num.start()-1, num.end()+1) for i in [-1,0,1]}
            for coord in coords:
                if dcomp.get(coord, ".") == "*":
                    seen[coord].append(int(num.group()))
    return sum(i[0]*i[1] for i in seen.values() if len(i) == 2)
