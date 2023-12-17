import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=4512)
def pt1(data_file):
    data = []
    lines = open(data_file).readlines()
    nums = [int(i) for i in lines[0].strip().split(",")]
    for i in lines[1:]:
        if i == "\n":
            data.append([])
        else:
            data[-1].append([int(i) for i in i.strip().split()])
    for num in nums:
        for idx,card in enumerate(data):
            data[idx] = card = np.where(np.equal(card, num), -1, card)
            if np.any(np.sum(card, 0)==-5) or np.any(np.sum(card, 1)==-5):
                return np.sum(np.where(card>=0, card, 0))*int(num)
        
        

@mark.solution(test=1924)
def pt2(data_file):
    data = []
    lines = open(data_file).readlines()
    nums = [int(i) for i in lines[0].strip().split(",")]
    for i in lines[1:]:
        if i == "\n":
            data.append([])
        else:
            data[-1].append([int(i) for i in i.strip().split()])
    lnum, lcard = None, None
    for num in nums:
        for idx,card in enumerate(data):
            if card is None:
                continue
            data[idx] = card = np.where(np.equal(card, num), -1, card)
            if np.any(np.sum(card, 0)==-5) or np.any(np.sum(card, 1)==-5):
                lnum,lcard = num,card
                data[idx] = None
    return np.sum(np.where(lcard>=0, lcard, 0))*lnum
        