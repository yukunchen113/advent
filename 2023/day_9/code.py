import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=114)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    total = 0
    for line in data:
        nums = [int(i) for i in line.split()]
        cum_nums = []        
        while not np.all(np.equal(nums, 0)):
            cum_nums.append(nums)
            nums = np.diff(nums)
        num = 0
        while cum_nums:
            num+=cum_nums.pop()[0]
        total+=num
    return total

@mark.solution(test=2)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    total = 0
    for line in data:
        nums = [int(i) for i in line.split()]
        cum_nums = []        
        while not np.all(np.equal(nums, 0)):
            cum_nums.append(nums)
            nums = np.diff(nums)
        num = 0
        while cum_nums:
            num=cum_nums.pop()[0]-num
        total+=num
    return total
        