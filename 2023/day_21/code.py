import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import math
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=None)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    data = convert_to_complex(data)
    nodes = [i for i,v in data.items() if v == "S"]
    
    for _ in range(65):
        nnodes = set()
        num_vals = 0
        for node in nodes:
            if node in data and data[node] != "#":
                num_vals += 1
                nnodes.add(node+1j)
                nnodes.add(node+1)
                nnodes.add(node-1)
                nnodes.add(node-1j)
        nodes = nnodes
    return num_vals
        
# @mark.solution(test=1594)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    bound = complex(len(data), len(data[-1]))
    data = convert_to_complex(data)
    nodes = {i:{0} for i,v in data.items() if v == "S"}
    for _ in range(26501365+1):
        nnodes = defaultdict(set) # n: boards
        num_vals = 0
        for node, boards in nodes.items():
            if node not in data:
                nr, ni = node.real, node.imag
                node = complex(node.real%bound.real, node.imag%bound.imag)
                if nr < 0:
                    boards = {i-1 for i in boards}
                elif nr >= bound.real:
                    boards = {i+1 for i in boards}
                elif ni < 0:
                    boards = {i-1j for i in boards}
                else:
                    boards = {i+1j for i in boards}
            if data[node] != "#":
                num_vals += len(boards)
                for dir in [1j,1,-1,-1j]:
                    nnodes[node+dir] = boards | nnodes[node+dir]
        nodes = nnodes
    print(num_vals)
    #return num_vals
    
@mark.solution(test=1591)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    bound = complex(len(data), len(data[-1]))
    data = convert_to_complex(data)
    nodes = [i for i,v in data.items() if v == "S"]
    
    pattern = defaultdict(list)
    prev_nv = 1
    prev_diff = 1
    unique_boards = set()
    for level in range(26501365+1):
        nnodes = set()
        num_vals = 0
        for node in nodes:
            if not node in data:
                unique_boards.add(complex(node.real%bound.real, node.imag%bound.imag))
            if data[complex(node.real%bound.real, node.imag%bound.imag)] != "#":
                num_vals += 1
                nnodes.add(node+1j)
                nnodes.add(node+1)
                nnodes.add(node-1)
                nnodes.add(node-1j)
        nodes = nnodes
        diff = num_vals-prev_nv
        # print(diff/prev_diff)
        # if diff/prev_diff in pattern:
        #     print(pattern[diff/prev_diff], level)
        # pattern[diff/prev_diff].append(level)
        print(diff)
        prev_nv = num_vals
        prev_diff = diff or 1
    # return num_vals

# @mark.solution(test=1591)
def pt2_dumb(data_file):
    data = [i.strip()*3 for i in open(data_file).readlines()]*3
    data = convert_to_complex(data)
    nodes = [(i,0) for i,v in data.items() if v == "S"]
    nodes = [(16j+16, 0)]
    for level in range(10+1):
        nnodes = set()
        num_vals = 0
        for node,board in nodes:
            if node in data and data[node] != "#":
                num_vals += 1
                nnodes.add((node+1j, board))
                nnodes.add((node+1, board))
                nnodes.add((node-1, board))
                nnodes.add((node-1j, board))
        nodes = nnodes
        print(level, num_vals)
    # return num_vals