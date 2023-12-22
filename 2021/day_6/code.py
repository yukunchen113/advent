import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=5934)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()][0]
    fishes = Counter([int(i) for i in data.split(",")])
    for _ in range(80):
        nfishes = defaultdict(lambda: 0)
        for days,num in fishes.items():
            nday = days - 1
            if not days:
                nfishes[8] = num
                nday = nday%7
            nfishes[nday] += num
        fishes = nfishes
    return sum(fishes.values())

@mark.solution(test=26984457539)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()][0]
    fishes = Counter([int(i) for i in data.split(",")])
    for _ in range(256):
        nfishes = defaultdict(lambda: 0)
        for days,num in fishes.items():
            nday = days - 1
            if not days:
                nfishes[8] = num
                nday = nday%7
            nfishes[nday] += num
        fishes = nfishes
    return sum(fishes.values())