import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex
import math

@mark.solution(test=168)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()][0].split(",")
    data = sorted(int(i) for i in data)
    mins = float("inf")
    for num in range(data[0], data[-1]):
        score = sum((abs(n-num)+1)*abs(n-num)/2 for n in data)
        mins = min(
            mins, 
            score
            )

    return mins
              
    
    