import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

valid = {
    1:"|LJ",
    -1j:"LF-",
    -1:"7F|",
    1j:"7-J"
}

@mark.solution(test=22)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    map = convert_to_complex(data)
    # get start coord
    nodes = [k for k,v in map.items() if v == "S"]
    assert len(nodes) == 1, nodes
    level = 0
    seen = set()
    while nodes:
        new_nodes = []
        for node in nodes:
            for dir, val in valid.items():
                if node+dir in map and map[node+dir] in val and not node+dir in seen:
                    new_nodes.append(node+dir)
                    seen.add(node+dir)
        nodes = new_nodes
        level +=1
        if len(nodes) == 1:
            return level

valid_half = {
    0.5:"|LJ",
    -0.5j:"LF-",
    -0.5:"7F|",
    0.5j:"7-J"
}

def get_inside_loop(loop, map):
    inside,outside = set(),set()
    for coord in map:
        if coord in loop or coord in outside or coord in inside: continue
        # check if outside
        considered = set()
        is_outside = False
        nodes = set([coord])
        while nodes:
            nnodes = set()
            for node in nodes:
                if node not in map or node in outside:
                    is_outside = True
                    continue
                if node in loop or node in considered:
                    continue
                considered.add(node)
                for dir in valid_half.keys():
                    nnodes.add(node+dir)
            nodes = nnodes
        if is_outside:
            outside = outside.union(considered)
        else:
            inside = inside.union(considered)
    return len([i for i in inside if not i.real%1 and not i.imag%1])

def expand_map(map):
    new_map = {}
    for coord, val in map.items():
        new_map[coord] = val
        new_map[coord+0.5j] = "-"
        new_map[coord+0.5] = "|" 
        new_map[coord+0.5j+0.5] = "."
    return new_map

half_dir = {
    "F":{0.5,0.5j},
    "L":{-0.5,0.5j},
    "7":{0.5,-0.5j},
    "J":{-0.5,-0.5j},
    "|":{-0.5,0.5},
    "-":{-0.5j,0.5j},
}

def get_s_replacement(map, node):
    dirs = set([k for k,v in valid.items() if map[node+k] in v])
    if dirs == {1,1j}:
        return "F"
    elif dirs == {-1,1j}:
        return "L"
    elif dirs == {1,-1j}:
        return "7"
    elif dirs == {-1,-1j}:
        return "J"
    elif dirs == {-1,1}:
        return "|"
    elif dirs == {-1j,1j}:
        return "-"

@mark.solution(test=4)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    map = convert_to_complex(data)
    map = expand_map(map)
    
    # get start coord
    nodes = [k for k,v in map.items() if v == "S"]
    map[nodes[0]] = get_s_replacement(map, nodes[0])
    assert len(nodes) == 1, nodes
    seen = set()
    while nodes:
        new_nodes = []
        for node in nodes:
            for dir, val in valid_half.items():
                if map[node] in half_dir and not dir in half_dir[map[node]]:
                    continue
                if node+dir in map and map[node+dir] in val and not node+dir in seen:
                    new_nodes.append(node+dir)
                    seen.add(node+dir)
        nodes = new_nodes
        if len(nodes) == 1:
            return get_inside_loop(seen, map)