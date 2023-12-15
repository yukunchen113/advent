import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=150)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    h,v = 0,0
    for d in data:
        dir,num = d.split()
        if dir.startswith("f"):
            h+=int(num)
        if dir.startswith("d"):
            v+=int(num)
        if dir.startswith("u"):
            v-=int(num)
    return h*v


@mark.solution(test=900)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    h,v,a = 0,0,0
    for d in data:
        dir,num = d.split()
        if dir.startswith("f"):
            h+=int(num)
            v+=int(num)*a
        if dir.startswith("d"):
            a+=int(num)
        if dir.startswith("u"):
            a-=int(num)
    return h*v