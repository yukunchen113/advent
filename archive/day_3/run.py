import os
from collections import defaultdict
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
import library

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

if __name__ == "__main__":
    tout = new_main('data_3.t')
    eout = 467835
    assert tout == eout, tout
    print("Test Success")
    mout = new_main('data_3.m')
    print("main: ", mout)
