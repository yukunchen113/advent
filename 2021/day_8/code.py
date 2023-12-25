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
    total = 0
    for line in data:
        for word in line.split(" | ")[1].split():
            if len(word) in [2,4,3,7]:
                total += 1
    return total

@mark.solution(test=61229)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    total = 0
    known = {2:"1",4:"4",3:"7",7:"8"}
    for line in data:
        num = ""
        kset = {}
        for signal in line.split(" | ")[0].split():
            dig = known.get(len(signal))
            if dig:
                kset[dig] = set(signal)
        for word in line.split(" | ")[1].split():
            dig = known.get(len(word))
            if not dig:
                if len(set(word)&kset["8"].difference(kset["4"]|kset["7"])) == 2:
                    if len(word) == 5:
                        dig = "2"
                    elif len(set(word)&kset["7"]) == 3:
                        dig = "0"
                    else:
                        dig = "6"
                elif len(set(word)&set(kset["1"])) == 1 and len(word) == 5:
                    dig = "5"
                elif len((set(kset["7"]) | set(kset["4"])) & set(word)) == 5:
                    dig = "9"
                else:
                    dig = "3"
            num+=dig
        print(num)
        total += int(num)
    return total