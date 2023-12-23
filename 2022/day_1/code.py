import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=None)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    max_sum = 0
    csum = 0
    for line in data:
        if line:
            csum+=int(line)
        else:
            max_sum = max(csum, max_sum)
            csum = 0
    max_sum = max(csum, max_sum)
    return max_sum

@mark.solution(test=None)
def faster_pt1(data_file):
    data = open(data_file).read()
    return max(
        sum(int(i) for i in line.split("\n") if i) 
        for line in data.split("\n\n"))

@mark.solution(test=None)
def faster_pt2(data_file):
    data = open(data_file).read()
    return sum(sorted(
        sum(int(i) for i in line.split("\n") if i) 
        for line in data.split("\n\n"))[-3:])
    
@mark.solution(test=45000)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    csum = 0
    sums = []
    for line in data:
        if line:
            csum+=int(line)
        else:
            sums.append(csum)
            csum = 0
    sums.append(csum)
    return sum(sorted(sums)[-3:])