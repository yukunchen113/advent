import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex
import sys
import uuid
sys.setrecursionlimit(15000)

@mark.solution(test=94)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    end = complex(len(data)-1, len(data[-1])-2)
    data = convert_to_complex(data)
    slopes = {"^":-1, ">":1j, "v":1, "<":-1j}
    seen = set()
    def longest(node):
        if node == end:
            return 0
        if node not in data or data[node] == "#" or node in seen:
            return -float("inf")
        s = data[node]
        seen.add(node)
        if s in slopes:
            out = longest(node+slopes[s])+1
        else:
            out = max(longest(node+i)+1
                for i in slopes.values())
        seen.remove(node)
        return out
    return longest(1j)


@mark.solution(test=154)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    end = complex(len(data)-1, len(data[-1])-2)
    data = convert_to_complex(data)
    seen = set() # seen central points
    # central points - start, end, fork
    adj = defaultdict(dict)
    def is_cp(node):
        valid_childs = [
            node+dir
            for dir in [1,-1,-1j,1j]
            if not (node+dir not in data or data[node+dir] == "#" or node+dir in seen)
        ]
        return len(valid_childs) > 1 or node in [1j, end] or node in adj
    def get_paths(cp, node, plen):
        if node not in data or data[node] == "#":
            return
        if is_cp(node) and cp != node:
            adj[node][cp] = plen
            adj[cp][node] = plen
            cp = node
            plen = 0
        if node == end:
            return 0
        if node in seen:
            return -float("inf")
        seen.add(node)
        for i in [-1,1j,-1j,1]:
            get_paths(cp, node+i, plen+1)
    get_paths(1j,1j,0)
    
    seen = set()
    def longest(node):
        if node == end:
            return 0
        if node in seen:
            return -float("inf")
        seen.add(node)
        out = max(longest(nnode)+plen
            for nnode, plen in adj[node].items())
        seen.remove(node)
        return out

    return longest(1j)