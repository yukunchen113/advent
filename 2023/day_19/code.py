import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
import copy
from advent import mark
from advent.tools.map import convert_to_complex


def getpmapitem(line):
    key = None
    val = []
    if line and not line.startswith("{"):
        key, nline = line.split("{")
        for match in nline[:-1].split(","):
            if "<" in match or ">" in match:
                n,d = match[2:].split(":")
                val.append((match[0], ((("<" in match)*(-1) or 1)*int(n), d)))
            else:
                val.append((".",(float("inf"), match)))
    return key, val

class Interval:
    def __init__(self, min=1, max=4000):
        # both are inclusive
        min,max = sorted([min,max])
        self.min = min
        self.max = max
        
    def __contains__(self, a):
        if isinstance(a, int):
            return self.min <= a <= self.max
        elif isinstance(a, Interval):
            return self.min <= a.min and self.max >= a.max
        else:
            raise TypeError(f"Unexpected type for contains {type(a)}")
        
    def __repr__(self):
        return f"Interval({self.min}, {self.max})"
    
    def increment(self, max=0, min=0):
        return Interval(self.min+min, self.max+max)
    
    def __add__(self, a):
        if a.max in self.increment(1, -1) or a.min in self.increment(1, -1):
            return [Interval(min(self.min, a.min), max(self.max, a.max))]
        return sorted([a, self], key=lambda x: (x.min, x.max))
        
    def __sub__(self, a):
        assert a in self, f"B must be in A, but is: B:{a}, A:{self}"
        x,y,z,w = sorted([a.min, a.max, self.min, self.max])
        output = []
        if x != y:
            output.append(Interval(x,y-1))
        if z != w:
            output.append(Interval(z+1,w))
        return output

    def intersect(self, a):
        if not (a.max in self or a.min in self):
            return None
        return Interval(max(self.min, a.min), min(a.max, self.max))

    def __eq__(self, a):
        return self.min == a.min and self.max == a.max
    def __len__(self):
        return self.max - self.min + 1
    def asrange(self):
        return range(self.min, self.max+1)

def getpmapintervals(line):
    key = None
    val = []
    if line and not line.startswith("{"):
        key, nline = line.split("{")
        for match in nline[:-1].split(","):
            if "<" in match or ">" in match:
                num,next_op = match[2:].split(":")
                intervals = {match[0]:None}
                if "<" in match:
                    intervals[match[0]] = [Interval(max=int(num)-1)]
                else:
                    intervals[match[0]] = [Interval(min=int(num)+1)]
            else:
                intervals = {}
                next_op = match
            val.append((intervals, next_op))
    return key, val

@mark.solution(test=167409079868000)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    pmap = {}
    for line in data:
        k,v  = getpmapintervals(line)
        if k is not None: 
            pmap[k] = v
    nodes = [("in", [(i,Interval()) for i in "xmas"])]
    total = 0
    while nodes:
        chain, cints = nodes.pop()
        if chain == "A":
            mul = 1
            for _,i in cints:
                mul*=len(i)
            total += mul
        elif chain != "R":
            for dcuts, nchain in pmap[chain]:
                ncints,rcints = [],[]
                for p, cint in cints:
                    if p in dcuts:
                        assert len(dcuts[p]) == 1
                        cutoff = dcuts[p][0]
                        isect = cint.intersect(cutoff)
                        if isect:
                            ncints.append((p,isect))
                            diff = cint-isect
                            if diff:
                                rcints.append((p,diff[0]))
                            else:
                                rcints.append((p,None))
                        else:
                            ncints.append((p,None))
                            rcints.append((p,cint))
                    else:
                        ncints.append((p,cint))
                        rcints.append((p,cint))
                if any(i[1] is None for i in ncints): # need to add one per part
                    continue
                nodes.append((nchain, ncints))
                if any(i[1] is None for i in rcints):
                    continue
                cints = rcints
                
    return total
    
