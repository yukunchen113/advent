from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=102)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    start, end = 0, complex(len(data)-1, len(data[-1])-1)
    data = convert_to_complex(data)
    seen = {}
    nodes = [(start+1j,1j,1,0), (start+1,1,1,0)]
    min_cost = float("inf")
    while nodes:
        nnodes = []
        for pos,dir,step,cost in sorted(nodes, key=lambda x: x[-1]):
            if pos not in data or step > 2:
                continue
            if (pos, dir, step) in seen and cost >= seen[(pos, dir, step)]:
                 continue
            if pos == end:
                min_cost = min(min_cost, cost + int(data[pos]))
                continue
            seen[(pos, dir, step)] = cost
            nnodes += [
                (pos+dir, dir, step+1, cost + int(data[pos])),
                (pos+dir*1j, dir*1j, 0, cost + int(data[pos])),
                (pos+dir*(-1j), dir*(-1j), 0, cost + int(data[pos]))
            ]
        nodes = nnodes
    return min_cost

@mark.solution(test=94)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    start, end = 0, complex(len(data)-1, len(data[-1])-1)
    data = convert_to_complex(data)
    seen = {}
    nodes = [(start+1j,1j,1,0), (start+1,1,1,0)]
    min_cost = float("inf")
    while nodes:
        nnodes = []
        for pos,dir,step,cost in sorted(nodes, key=lambda x: x[-1]):
            if pos not in data or step > 9:
                continue
            if (pos, dir, step) in seen and cost >= seen[(pos, dir, step)]:
                continue
            if pos == end:
                min_cost = min(min_cost, cost + int(data[pos]))
                continue
            seen[(pos, dir, step)] = cost
            nnodes.append((pos+dir, dir, step+1, cost + int(data[pos])))
            if step >= 3:
                nnodes += [
                    (pos+dir*1j, dir*1j, 0, cost + int(data[pos])),
                    (pos+dir*(-1j), dir*(-1j), 0, cost + int(data[pos]))
                ]
        nodes = nnodes
    return min_cost