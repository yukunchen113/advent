import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex
import math

@mark.solution(test=11687500)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    nstate = [{}, {}] # fflop, conj
    pmap = {}
    for line in data:
        nfrom, ntos = line.split(" -> ")
        ntos = ntos.split(", ")
        if nfrom[0] in "%&":
            nstate[nfrom[0] == "&"][nfrom[1:]] = False if nfrom[0] == "%" else {}
            nfrom = nfrom[1:]
        pmap[nfrom] = ntos
    
    # populate conjs with connections
    for k,vals in pmap.items():
        for v in vals:
            if v in nstate[1]:
                nstate[1][v][k] = False

    total = [0, 0]
    for _ in range(1000):
        total[0] += 1
        nodes = [("broadcaster", 0)]
        while nodes:
            nnodes = []
            for node,sig in nodes:
                if node in nstate[1]:
                    sig = nstate[1][node] and not all(nstate[1][node].values())
                if node in nstate[0]:
                    sig = nstate[0][node]
                for nnode in pmap.get(node, []):
                    total[sig]+=1
                    if nnode in nstate[0]:
                        nsig = None
                        nstate[0][nnode] = not nstate[0][nnode] ^ sig
                        if not sig:
                            nnodes.append((nnode, nsig))
                    elif nnode in nstate[1]:
                        nsig = None
                        nstate[1][nnode][node] = sig
                        nnodes.append((nnode, nsig))
            nodes = nnodes
    return np.prod(total)
    

@mark.solution(test=None)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    nstate = [{}, {}] # fflop, conj
    pmap = {}
    for line in data:
        nfrom, ntos = line.split(" -> ")
        ntos = ntos.split(", ")
        if nfrom[0] in "%&":
            nstate[nfrom[0] == "&"][nfrom[1:]] = False if nfrom[0] == "%" else {}
            nfrom = nfrom[1:]
        pmap[nfrom] = ntos
    
    # populate conjs with connections
    for k,vals in pmap.items():
        for v in vals:
            if v in nstate[1]:
                nstate[1][v][k] = False

    total = [0, 0]
    step = 0
    mfstate = {}
    while True:
        step += 1
        total[0] += 1
        nodes = [("broadcaster", 0)]
        while nodes:
            nnodes = []
            for node,sig in nodes:
                if node in nstate[1]:
                    sig = nstate[1][node] and not all(nstate[1][node].values())
                if node in nstate[0]:
                    sig = nstate[0][node]
                for nnode in pmap.get(node, []):
                    if nnode == "rx":
                        for k,v in nstate[1]["mf"].items():
                            if v and not isinstance(mfstate.get(k), list):
                                if not k in mfstate and step != 1:
                                    mfstate[k] = step
                        if len(mfstate) == 4:
                            return math.lcm(*mfstate.values())
                    total[sig]+=1
                    if nnode in nstate[0]:
                        nsig = None
                        nstate[0][nnode] = not nstate[0][nnode] ^ sig
                        if not sig:
                            nnodes.append((nnode, nsig))
                    elif nnode in nstate[1]:
                        nsig = None
                        nstate[1][nnode][node] = sig
                        nnodes.append((nnode, nsig))
            nodes = nnodes