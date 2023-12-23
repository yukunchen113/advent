import os
from collections import defaultdict


def parse_input(data_file):
    with open(data_file) as f:
        lines = [i.replace("\n", "") for i in f.readlines()]

    bound = complex(len(lines)-1, len(lines[0])-1)
    blizzard = []
    for ridx, row in enumerate(lines):
        for cidx, ele in enumerate(row):
            pos = complex(ridx, cidx)
            if ele == ">":
                blizzard.append((pos,1j))
            elif ele == "<":
                blizzard.append((pos,-1j))
            elif ele == "^":
                blizzard.append((pos,-1))
            elif ele == "v":
                blizzard.append((pos,1))
    return blizzard, bound

def move_with_wrap(pos,dir,bound):
    pos = pos + dir
    if dir == 1j and pos.imag == bound.imag:
        pos = complex(pos.real, 1)
    elif dir == -1j and pos.imag == 0:
        pos = complex(pos.real, bound.imag - 1)
    elif dir == -1 and pos.real == 0:
        pos = complex(bound.real-1, pos.imag)
    elif dir == 1 and pos.real == bound.real:
        pos = complex(1, pos.imag)
    return pos

def iterate_blizzard(blizzard, bound):
    new_blizzard = []
    for pos, dir in blizzard:
        new_blizzard.append((move_with_wrap(pos,dir,bound), dir))
    return new_blizzard

def is_valid_pos(pos, blizzard, bound):
    blizzard_pos = set(i[0] for i in blizzard)
    return (
        pos in (1j, bound - 1j) or
        pos not in blizzard_pos
        and 0 < pos.imag < bound.imag
        and 0 < pos.real < bound.real
    )

def travel(blizzard, bound, start, end):
    level = set([start])
    min_passed = 0
    seen_pos = set()
    while level:
        new_level = set()
        next_blizzard = iterate_blizzard(blizzard, bound)
        next_blizard_hash = tuple(sorted([(i.real, i.imag, d.real, d.imag) for i,d in next_blizzard]))
        for pos in level:
            if pos == end:
                return min_passed, blizzard
            if is_valid_pos(pos, next_blizzard, bound) and not (pos, next_blizard_hash) in seen_pos:
                new_level.add(pos)
            seen_pos.add((pos, next_blizard_hash))
            for dir in [1,-1,-1j,1j]:
                if is_valid_pos(pos+dir, next_blizzard, bound) and not (pos+dir, next_blizard_hash) in seen_pos:
                    new_level.add(pos+dir)
        level = new_level
        min_passed += 1
        blizzard = next_blizzard


def main(data_file):
    blizzard, bound = parse_input(data_file)
    start = 1j
    end = bound - 1j
    min1, blizzard = travel(blizzard, bound, start, end)
    min2, blizzard = travel(blizzard, bound, end, start)
    min3, blizzard = travel(blizzard, bound, start, end)
    return sum([min1,min2,min3])



SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_24.t')
    eout = 54
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_24.m')
    print("main: ", mout)
