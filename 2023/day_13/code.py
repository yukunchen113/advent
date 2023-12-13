import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=405)
def pt1(data_file):
    data = [[]]
    for i in open(data_file).readlines():
        if i =="\n":
            data.append([])
        else:
            data[-1].append(list(i.strip()))
    total = 0
    for pat in data:
        pat = np.array(pat)
        # check row
        for idx in range(pat.shape[0]-1):
            length = min(pat.shape[0]-(idx+1), idx+1)
            if np.all(pat[idx+1-length:idx+1] == np.flip(pat[idx+1:idx+1+length], 0)):
                total += 100*(idx+1)
        # check col
        for idx in range(pat.shape[1]-1):
            length = min(pat.shape[1]-(idx+1), idx+1)
            if np.all(pat[:, idx+1-length:idx+1] == np.flip(pat[:,idx+1:idx+1+length], 1)):
                total += idx+1
    return total

@mark.solution(test=400)
def pt2(data_file):
    data = [[]]
    for i in open(data_file).readlines():
        if i =="\n":
            data.append([])
        else:
            data[-1].append(list(i.strip()))
    total = 0
    for pat in data:
        pat = np.array(pat)
        # check row
        for idx in range(pat.shape[0]-1):
            length = min(pat.shape[0]-(idx+1), idx+1)
            if np.sum(pat[idx+1-length:idx+1] != np.flip(pat[idx+1:idx+1+length], 0)) == 1:
                total += 100*(idx+1)
        # check col
        for idx in range(pat.shape[1]-1):
            length = min(pat.shape[1]-(idx+1), idx+1)
            if np.sum(pat[:, idx+1-length:idx+1] != np.flip(pat[:,idx+1:idx+1+length], 1)) == 1:
                total += idx+1
    return total
