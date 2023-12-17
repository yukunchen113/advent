import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=5)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    points = defaultdict(lambda: 0)
    for line in data:
        x1,y1,x2,y2 = re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", line)[0]
        x1,x2 = sorted([int(x1),int(x2)])
        y1,y2 = sorted([int(y1),int(y2)])
        if x1 == x2:
            for dy in range(y1, y2+1):
                points[(dy, x1)] += 1
        if y1 == y2:
            for dx in range(x1, x2+1):
                points[(y1, dx)] += 1
    return len([v for v in points.values() if v >= 2])

@mark.solution(test=12)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    points = defaultdict(lambda: 0)
    for line in data:
        x1,y1,x2,y2 = re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", line)[0]
        x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
        if x1 == x2:
            y1,y2 = sorted([y1,y2])
            for dy in range(y1, y2+1):
                points[(dy, x1)] += 1
        elif y1 == y2:
            x1,x2 = sorted([x1,x2])
            for dx in range(x1, x2+1):
                points[(y1, dx)] += 1
        else:
            for step in range(abs(x2-x1)+1):
                dx, dy = x2 - x1, y2 - y1
                points[(y1+dy*step/abs(dy), x1+dx*step/abs(dx))] += 1
            
    return len([v for v in points.values() if v >= 2])


