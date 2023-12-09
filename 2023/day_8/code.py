import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import math
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex    

@mark.solution(test=6)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    insts, lines = data[0], data[2:]
    mapping = {}
    for line in lines:
        nums = re.findall(r"(...) = \((...), (...)\)", line)[0]
        mapping[nums[0]] = {"L":nums[1], "R":nums[2]}
    
    nodes = {i:None for i in mapping.keys() if i.endswith("A")}
    inum = 0
    while not all(node.endswith("Z") for node in nodes.keys()):
        new_nodes = {}
        while nodes:
            node,val = nodes.popitem()
            new_nodes[mapping[node][insts[inum%len(insts)]]] = val
            if node.endswith("Z"):
                if val is None:
                    new_nodes[mapping[node][insts[inum%len(insts)]]] = [inum, None]
                elif val[1] is None:
                    new_nodes[mapping[node][insts[inum%len(insts)]]][1] = inum - val[0]
        nodes = new_nodes
        if all(val and val[1] for val in nodes.values()):
            return math.lcm(*[i[0] for i in nodes.values()]) # hacky, assumes that Z points to A
        inum+=1
    return inum
        
        
@mark.solution(test=6)
def efficient_pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    insts, lines = data[0], data[2:]
    mapping = {}
    for line in lines:
        print(re.findall(r"[A-Za-z0-9]{3}", line))
        k,l,r = re.findall(r"[A-Za-z0-9]{3}", line)
        mapping[k] = {"L":l, "R":r}
        
    nodes = [i for i in mapping.keys() if i.endswith("A")]
    cycles = {}
    inum = 0
    while len(cycles) != len(nodes):
        new_nodes = []
        for node in nodes:
            new_nodes.append(mapping[node][insts[inum%len(insts)]])
            if new_nodes[-1].endswith("Z") and not new_nodes[-1] in cycles:
                cycles[new_nodes[-1]] = inum+1
        nodes = new_nodes
        inum += 1 
    return math.lcm(*cycles.values())