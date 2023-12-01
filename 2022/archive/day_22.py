import os
import re
from collections import defaultdict
from copy import deepcopy
from pprint import pprint
from functools import cache

def process_map(map, edge_len):
    # get adjacency matrix
    start = complex(0, map[0].index("."))
    adjs = {}
    def inital_adj(point):
        if (
            not (0 <= point.real < len(map)) 
            or not (0 <=point.imag <len(map[int(point.real)]))
            or map[int(point.real)][int(point.imag)] not in ".#"
        ):
            return None
        if point in adjs:
            return True
        adjs[point] = {}
        for i in [1,-1j,-1,1j]:
            if inital_adj(point+edge_len*i):
                adjs[point][i] = [point+edge_len*i, i]
        return True
    inital_adj(start)
    pprint(adjs)
    
    # directional transformations
    for _ in range(8):
        for node, ladj in deepcopy(adjs).items():
            for nodedir,(cornode,cordir) in deepcopy(ladj).items():
                for newdir in [1j, -1j]:
                    cornerchilddir = newdir*cordir # direction of child from perspective of corner node
                    if cornerchilddir in adjs[cornode]:
                        if not nodedir*newdir in adjs[node]:
                            newnode, newdirfromcorner = adjs[cornode][cornerchilddir]
                            newdirfromnode = newdirfromcorner/newdir
                            adjs[node][nodedir*newdir] = [newnode, newdirfromnode]
    return adjs

def get_pos_face(pos, adjs, side_len):
    for face in adjs.keys():
        if face.real <=pos.real<(face.real+side_len) and face.imag <=pos.imag<(face.imag+side_len):
            return face
    return None

def get_face_side_origin(dir, face, side_len, is_source):
    if is_source:
        if dir.real == -1 or dir.imag == -1:
            return face + 1*dir
        else:
            return face + side_len*dir
    else:
        if (dir.real+dir.imag) > 0: 
            return face
        else:
            return face+(side_len-1)*(-dir)
    

def calculate_new_position(pos,npos,dir, adjs, side_len):
    face = get_pos_face(pos, adjs, side_len)
    assert face, f"No face found for {pos}."
    nface, ndir = adjs[face][dir]
    # get face side origin
    side_origin = get_face_side_origin(dir, face, side_len, True)
    # get length by subtracting from face side origin
    length = npos - side_origin
    assert not length.real or not length.imag
    if dir*ndir == 1j or dir/ndir == -1: 
        # flip length
        length = length - ((side_len-1)*(1j if length.imag else 1))
    # get length orientation
    length = length*ndir/dir    
    
    # get new face side origin
    nside_origin = get_face_side_origin(ndir, nface, side_len, False)
    # add length to new face side origin
    npos = nside_origin+length
    return npos, ndir
    
    
    

def parse_input(data_file):
    with open(data_file) as f:
        lines = f.readlines()
    map = [i.replace("\n", "") for i in lines[:-2]]
    max_len = max([len(i) for i in map])
    map = [i+" "*(max_len-len(i)) for i in map]
    inst = re.findall("(\d+|R|L)", lines[-1])
    inst = [i if i in "RL" else int(i) for i in inst]
    return map, inst

CUBE_FACE_MAPPING = None

def move_with_wrap(pos, dir, map):
    npos = pos+dir
    # check outside bounds
    is_wrap = False
    if (
        0 > npos.real
        or npos.real >= len(map)
        or 0 > npos.imag
        or npos.imag >= len(map[int(npos.real)])
        or map[int(npos.real)][int(npos.imag)] == " "
    ):
        is_wrap = True
    if is_wrap:
        sidelen = 4 if len(map)<50 else 50
        global CUBE_FACE_MAPPING
        if CUBE_FACE_MAPPING is None:
            CUBE_FACE_MAPPING = process_map(map, edge_len=sidelen)
        npos,ndir = calculate_new_position(pos,npos,dir,CUBE_FACE_MAPPING,sidelen)
    else:
        ndir=dir
    return npos, ndir

def move(pos, dir, inst, map):
    for _ in range(inst):
        npos,ndir=move_with_wrap(pos,dir,map)
        # map wrap around
        assert map[int(npos.real)][int(npos.imag)] != " "
        if map[int(npos.real)][int(npos.imag)] == "#":
            break
        pos = npos
        dir = ndir
    return pos, dir

def rotate(cur, inst):
    assert inst in "RL"
    return cur * (-1j if inst == "R" else 1j)

def main(data_file):
    map, instructions = parse_input(data_file)
    # begin at the leftmost open tile on top row
    pos, dir = complex(0, map[0].index(".")), complex(0, 1)
    for inst in instructions:
        if isinstance(inst, str):
            dir = rotate(dir, inst)
        else:
            pos, dir = move(pos, dir, inst, map)
            assert map[int(pos.real)][int(pos.imag)] == "."
    return int(1000*(pos.real+1)+4*(pos.imag+1)+[1j,1,-1j,-1].index(dir))


SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_22.t')
    eout = 5031
    assert tout == eout, tout
    print("Test Success")
    CUBE_FACE_MAPPING=None
    mout = main('data_22.m')
    print("main: ", mout)
