import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex
import networkx as nx
# @mark.solution(test=54)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    adj = defaultdict(set)
    connections = set()
    for line in data:
        head, comps = line.split(": ")
        for next in comps.split():
            adj[head].add(next)
            adj[next].add(head)
            connections.add(tuple(sorted([head,next])))
            
    def get_num_nodes(node):
        nodes = {node}
        seen = set()
        while nodes:
            nnodes = set()
            for node in nodes:
                if node not in seen:
                    seen.add(node)
                    nnodes = nnodes | adj[node]
            nodes = nnodes
        return len(seen)
        
    total = len(adj)
    connections = list(connections)
    for idx, (a1,b1) in enumerate(connections[:-2]):
        adj[a1].remove(b1)
        for jdx, (a2,b2) in enumerate(connections[idx+1:-1], idx+1):
            adj[a2].remove(b2)
            for a3,b3 in connections[jdx+1:]:
                adj[a3].remove(b3)
                num = get_num_nodes(list(adj.keys())[0])
                if num != total:
                    return (total-num)*num
                adj[a3].add(b3)
            adj[a2].add(b2)
        adj[a1].add(b1)
            
@mark.solution(test=54)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    graph = nx.DiGraph()
    nodes = set()
    for line in data:
        head, comps = line.split(": ")
        for next in comps.split():
            nodes.add(next)
            nodes.add(head)
            graph.add_edge(head, next, capacity=1)
            graph.add_edge(next, head, capacity=1)
    
    nodes = list(nodes)
    n1 = nodes[0]
    for n2 in nodes:
        if n1 == n2: continue
        cv, output = nx.minimum_cut(graph, n1, n2)
        if cv == 3:
            return len(output[1])*len(output[0])
            
    