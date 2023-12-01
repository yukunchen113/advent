import os
import re
from collections import defaultdict


def parse_input(data_file):
    with open(data_file) as f:
        lines = f.readlines()
    map = [i.replace("\n", "") for i in lines[:-2]]
    max_len = max([len(i) for i in map])
    map = [i+" "*(max_len-len(i)) for i in map]
    inst = re.findall("(\d+|R|L)", lines[-1])
    inst = [i if i in "RL" else int(i) for i in inst]
    return map, inst

def move_with_wrap(pos, dir, map):
    pos:complex=dir + pos
    if 0 > pos.real:
        assert dir.imag == 0
        pos = complex(len(map)-1, pos.imag)
    elif pos.real >= len(map):
        assert dir.imag == 0
        pos = complex(0, pos.imag)
    elif 0 > pos.imag:
        assert dir.real == 0
        pos = complex(pos.real, len(map[int(pos.real)]) -1)
    elif pos.imag >= len(map[int(pos.real)]):
        assert dir.real == 0
        pos = complex(pos.real, 0)
    return pos

def move(pos, dir, inst, map):
    for _ in range(inst):
        npos:complex=move_with_wrap(pos,dir,map)
        # map wrap around
        while map[int(npos.real)][int(npos.imag)] == " ":
            npos=move_with_wrap(npos,dir,map)
            if npos == move_with_wrap(pos,dir,map):
                raise ValueError("Cycle of spaces in map")
        if map[int(npos.real)][int(npos.imag)] == "#":
            break
        assert pos.real == npos.real or pos.imag == npos.imag
        pos = npos
    return pos

DIRECTIONS = [complex(0, 1), complex(1, 0), complex(0, -1), complex(-1, 0)]
def rotate(cur, inst):
    assert inst in "RL"
    return DIRECTIONS[(DIRECTIONS.index(cur) + (-1 if inst == "L" else 1)) % len(DIRECTIONS)]


def main(data_file):
    map, instructions = parse_input(data_file)
    # begin at the leftmost open tile on top row
    pos, dir = complex(0, map[0].index(".")), complex(0, 1)
    for inst in instructions:
        if isinstance(inst, str):
            dir = rotate(dir, inst)
        else:
            pos = move(pos, dir, inst, map)
            assert map[int(pos.real)][int(pos.imag)] == "."
    return int(1000*(pos.real+1)+4*(pos.imag+1)+DIRECTIONS.index(dir))


SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_22.t')
    eout = 6032
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_22')
    print("main: ", mout)
