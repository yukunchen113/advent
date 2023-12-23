from collections import defaultdict
from advent import mark
import copy

@mark.solution(test=5)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    bricks = []
    for bnum, line in enumerate(data):
        s,e = line.split("~")
        x1,y1,z1 = [int(i) for i in s.split(",")]
        x2,y2,z2 = [int(i) for i in e.split(",")]
        x1,x2 = sorted([x1,x2])
        y1,y2 = sorted([y1,y2])
        z1,z2 = sorted([z1,z2])
        bricks.append((z1, z2-z1+1, [(i,j) for i in range(x1, x2+1) for j in range(y1, y2+1)], bnum))
    
    support = defaultdict(set)
    pblocks = {}
    cpoints = defaultdict(lambda: 0)
    for _, zlen, points, bnum in sorted(bricks):
        maxz = max(cpoints[point] for point in points)
        for point in points:
            if point in pblocks and cpoints[point] == maxz:
                support[bnum].add(pblocks[point])
            cpoints[point] = maxz + zlen
            pblocks[point] = bnum
    
    needed = set()
    for _, sups in support.items():
        if len(sups) == 1:
            needed = needed | sups
            
    return len({i for i in range(len(bricks)) if i not in needed})

@mark.solution(test=7)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    bricks = []
    for bnum, line in enumerate(data):
        s,e = line.split("~")
        x1,y1,z1 = [int(i) for i in s.split(",")]
        x2,y2,z2 = [int(i) for i in e.split(",")]
        x1,x2 = sorted([x1,x2])
        y1,y2 = sorted([y1,y2])
        z1,z2 = sorted([z1,z2])
        bricks.append((z1, z2-z1+1, [(i,j) for i in range(x1, x2+1) for j in range(y1, y2+1)], bnum))
    
    support = defaultdict(set)
    pblocks = {}
    cpoints = defaultdict(lambda: 0)
    for _, zlen, points, bnum in sorted(bricks):
        maxz = max(cpoints[point] for point in points)
        for point in points:
            if point in pblocks and cpoints[point] == maxz:
                support[bnum].add(pblocks[point])
            cpoints[point] = maxz + zlen
            pblocks[point] = bnum

    total = 0
    for i in range(len(bricks)):
        csups = copy.deepcopy(support)
        nodes = {i}
        while nodes:
            node = nodes.pop()
            for b, sups in csups.items():
                if not len(sups):
                    continue
                if node in sups:
                    sups.remove(node)
                if not len(sups):
                    nodes.add(b)
            csups = {b:c for b,c in csups.items() if c}
        total+=len(support)-len(csups)
    return total