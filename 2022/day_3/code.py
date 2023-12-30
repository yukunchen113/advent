import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=157)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    sum = 0
    for line in data:
        mid = len(line)//2
        out = min(ord(i)-ord("A")+27 if i == i.upper() else ord(i) - ord("a") +1 for i in line[:mid] if i in line[mid:])
        sum += out
    return sum

@mark.solution(test=70)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    common = []
    for idx,line in enumerate(data):
        eles = set(line)
        if not idx % 3:
            common.append(eles)
        else:
            common[-1] = eles & common[-1]
    common = [i.pop() for i in common]
    return sum(ord(i)-ord("A")+27 if i == i.upper() else ord(i) - ord("a") +1
            for i in common)