from collections import defaultdict
from advent import mark
        
@mark.solution(test=62)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    inst_map = {"R":1j,"D":1,"L":-1j,"U":-1}
    # get perimeter
    perimeter = set()
    pos = 0
    perimeter.add(0)
    for line in data:
        inst, units = line.split()[:-1]
        for _ in range(int(units)):
            pos += inst_map[inst]
            perimeter.add(pos)
    nodes, seen = {sorted(perimeter, key=lambda x: (x.real, x.imag))[0] + 1+1j}, set()
    while nodes:
        nnodes = set()
        for node in nodes:
            if node not in seen and node not in perimeter:
                seen.add(node)
                nnodes = nnodes | {node + i for i in [1,-1j,-1,1j]}
        nodes = nnodes
    return len(seen) +len(perimeter)

def combined(ints1, ints2):
    output = []
    for s,e in sorted(ints1+ints2):
        if not output or s>output[-1][1]:
            output.append([s,e])
        else:
            output[-1][1] = max(e, output[-1][1])
    return output

@mark.solution(test=952408144115)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    inst_map = {"0":1j,"1":1,"2":-1j,"3":-1}
    # get horzontal lines
    hlines = defaultdict(list)
    pos = 0
    for line in data:
        line = line.split()[-1][2:-1]
        units, inst = line[:-1], line[-1]
        npos = pos+inst_map[inst]*int(units, 16)
        if inst in "02":
            hlines[pos.real].append(sorted([pos.imag, npos.imag]))
        pos = npos
    lasth = []
    prev_k = total = 0
    for k in sorted(hlines.keys()):
        nlasth = []
        for s,e in lasth:
            total+=(e+1-s)*(k-prev_k-1)
        for s,e in sorted(lasth+hlines[k]):
            if nlasth and nlasth[-1][1] >= s:
                if nlasth[-1][1] > s:
                    nlasth += [sorted([a,b]) for a,b in zip([s,e],nlasth.pop()) if a != b]
                else:
                    nlasth[-1][1] = e
            else:
                nlasth.append([s,e])
        for s,e in combined(lasth,nlasth): 
            total+=e+1-s
        prev_k, lasth = k, nlasth
    return int(total)
