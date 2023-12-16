import os
from collections import defaultdict, Counter
from advent import mark
from advent.tools.map import convert_to_complex

def get_new_dirs(ref, dir):
    # this was used in comp
    dirs = []
    if (ref, dir) in {
        ("/",-1j),
        ("\\",1j),
        ("|",1j),
        ("|",-1j),
    }:
        dirs.append(1)
    if (ref, dir) in {
        ("/",1),
        ("\\", -1),
        ("-",1),
        ("-",-1)
    }:
        dirs.append(-1j)
    if (ref, dir) in {
        ("/",1j),
        ("\\",-1j),
        ("|",1j),
        ("|",-1j),
    }:
        dirs.append(-1)
    if (ref, dir) in {
        ("/",-1),
        ("\\",1),
        ("-",1),
        ("-",-1)
    }:
        dirs.append(1j)
    if not dirs:
        dirs = [dir]
    return dirs

def get_new_dirs_concise(ref, dir):
    dirs = set()
    if ref == "/":
        dirs.add(complex(-dir.imag, -dir.real))
    elif ref == "\\":
        dirs.add(complex(dir.imag, dir.real))
    elif ref == "|":
        dirs = dirs | {1,-1}
    elif ref == "-":
        dirs = dirs | {1j,-1j}
    else:
        dirs.add(dir)
    return dirs

@mark.solution(test=46)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    data = convert_to_complex(data)
    seen = set() # pos, dir
    nodes = [(0, 1j)]
    while nodes:
        nnodes = []
        for pos,dir in nodes:
            if pos not in data or (pos, dir) in seen:
                continue
            seen.add((pos,dir))
            dirs = get_new_dirs_concise(data[pos], dir)
            nnodes+=[(pos+dir, dir) for dir in dirs]
        nodes = nnodes
    return len(set(i[0] for i in seen))

def get_tiles(start, data):
    seen = set() # pos, dir
    nodes = [start]
    while nodes:
        nnodes = []
        for pos,dir in nodes:
            if pos not in data or (pos, dir) in seen:
                continue
            seen.add((pos,dir))
            dirs = get_new_dirs_concise(data[pos], dir)
            nnodes+=[(pos+dir, dir) for dir in dirs]
        nodes = nnodes
    return len(set(i[0] for i in seen))

@mark.solution(test=51)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    data = convert_to_complex(data)
    rb,ib = max((i.real, i.imag) for i in data.keys())
    return max(
        max(get_tiles((pos, 1j), data) for pos in data if pos.imag == 0),
        max(get_tiles((pos, -1j), data) for pos in data if pos.imag == ib),
        max(get_tiles((pos, 1), data) for pos in data if pos.real == 0),
        max(get_tiles((pos, -1), data) for pos in data if pos.real == rb)
    )