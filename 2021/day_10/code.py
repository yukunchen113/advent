import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=26397)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    mapping = {
        "{":"}",
        "(":")",
        "<":">",
        "[":"]",}
    total = 0
    for line in data:
        stack = []
        for char in line:
            if char in "{[(<":
                stack.append(mapping[char])
            else:
                last = stack.pop()
                if last != char:
                    if char == "}":
                        total += 1197
                    elif char == ")":
                        total += 3
                    elif char == "]":
                        total += 57
                    elif char == ">":
                        total += 25137
    return total



@mark.solution(test=288957)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    mapping = {
        "{":"}",
        "(":")",
        "<":">",
        "[":"]",}
    total = []
    scores = ".)]}>"
    for line in data:
        stack = []
        for char in line:
            if char in "{[(<":
                stack.append(mapping[char])
            else:
                last = stack.pop()
                if last != char:
                    stack = []
                    break
        score = 0
        while stack:
            bra = stack.pop()
            score = score*5+scores.index(bra)
        if score:
            total.append(score)
    total = sorted(total)
    return total[len(total)//2]