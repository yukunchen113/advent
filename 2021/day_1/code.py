import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=7)
def pt1(data_file):
    data = [int(i.strip()) for i in open(data_file).readlines()]
    return sum(data[idx+1]>val for idx,val in enumerate(data[:-1]))

@mark.solution(test=5)
def pt2(data_file):
    data = [int(i.strip()) for i in open(data_file).readlines()]
    return sum((data[idx+1]+data[idx+2]+data[idx+3])>(val+data[idx+1]+data[idx+2]) for idx,val in enumerate(data[:-3]))