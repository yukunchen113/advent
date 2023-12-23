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
    data = open(data_file).read()
    rps = [1,2,3]
    score = 0
    for round in data.split("\n"):
        if not round:
            continue
        o,m = round.split(" ")
        o = ord(o) - ord("A")
        m = ord(m) - ord("X")
        if m == (o+1)%3:
            score += rps[m] + 6
        elif m == o:
            score += 3 + rps[m]
        else:
            score += rps[m]
    return score

@mark.solution(test=12)
def pt2(data_file):
    data = open(data_file).read()
    rps = [1,2,3]
    score = 0
    for round in data.split("\n"):
        if not round:
            continue
        o,l = round.split(" ")
        o = ord(o) - ord("A")
        if l == "X":
            score += rps[(o-1)%3]
        elif l == "Y":
            score += 3 + rps[o]
        else:
            score += rps[(o+1)%3] + 6
    return score