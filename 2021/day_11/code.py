import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=1656)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    data = {k:int(v) for k,v in convert_to_complex(data).items()}
    
    def flash(k, pflash):
        if data[k] > 9 and k not in pflash:
            pflash.add(k)
            for dir in [-1,-1j,1,1j,-1-1j,-1+1j,1+1j,1-1j]:
                if k+dir in data:
                    data[k+dir] += 1
                    flash(k+dir, pflash)
    
    total = 0
    for step in range(1,101):
        already_flashed = set()
        for k in data.keys():
            data[k]+=1
            if data[k] > 9:
                flash(k, already_flashed)
        total += len(already_flashed)
        for k in already_flashed:
            data[k] = 0
    return total

@mark.solution(test=195)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    data = {k:int(v) for k,v in convert_to_complex(data).items()}
    
    def flash(k, pflash):
        if data[k] > 9 and k not in pflash:
            pflash.add(k)
            for dir in [-1,-1j,1,1j,-1-1j,-1+1j,1+1j,1-1j]:
                if k+dir in data:
                    data[k+dir] += 1
                    flash(k+dir, pflash)
    
    total = 0
    for step in range(1,1000):
        already_flashed = set()
        for k in data.keys():
            data[k]+=1
            if data[k] > 9:
                flash(k, already_flashed)
        total += len(already_flashed)
        if len(already_flashed) == len(data):
            return step
        for k in already_flashed:
            data[k] = 0
    return total