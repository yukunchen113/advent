import os
from collections import defaultdict


def parse_input(data_file):
    with open(data_file) as f:
        lines = f.readlines()
    return lines[0].strip('\n')


def simulate_step(rock, board, direct):
    # move x
    if direct == "<":
        # move left
        nrock = set([(r, c-1) for r,c in rock])
    elif direct == ">":
        # move right
        nrock = set([(r, c+1) for r,c in rock])
    else:
        nrock = rock
    for r,c in nrock:
        # if hit wall or hit rock
        if (
            0 > c or c >= 7
            or (r,c) in board
            ):
            nrock = rock
            break
    rock = nrock

    # move y
    bottom = False
    nrock = set([(r-1, c) for r,c in nrock])
    for r,c in nrock:
        # if hit floor or hit rock
        if (
            0 > r
            or (r,c) in board
            ):
            nrock = rock
            bottom = True
            break

    return nrock, bottom

def get_rock(origin, rnum):
    if rnum == 0:
        return set([
            (origin[0], origin[1]),
            (origin[0], origin[1]+1),
            (origin[0], origin[1]+2),
            (origin[0], origin[1]+3),]
        )
    elif rnum == 1:
        return set([
            (origin[0]+1, origin[1]),
            (origin[0], origin[1]+1),
            (origin[0]+1, origin[1]+1),
            (origin[0]+2, origin[1]+1),
            (origin[0]+1, origin[1]+2),]
        )
    elif rnum == 2:
        return set([
            (origin[0], origin[1]),
            (origin[0], origin[1]+1),
            (origin[0], origin[1]+2),
            (origin[0]+1, origin[1]+2),
            (origin[0]+2, origin[1]+2),]
        )
    elif rnum == 3:
        return set([
            (origin[0], origin[1]),
            (origin[0]+1, origin[1]),
            (origin[0]+2, origin[1]),
            (origin[0]+3, origin[1]),]
        )
    elif rnum == 4:
        return set([
            (origin[0], origin[1]),
            (origin[0], origin[1]+1),
            (origin[0]+1, origin[1]),
            (origin[0]+1, origin[1]+1),]
        )

def simulate(nrocks, wind):
    board = set()
    wind_step = 0
    for rnum in range(nrocks):
        # get init rock
        # get tallest rock - 3 away
        height = -1 if not len(board) else max([i for i,j in board])
        # origin = (tallest rock + 4, 2)
        origin = (height + 4, 2)
        # get rock
        rock = get_rock(origin, rnum%5)
        while rock is not None:
            # simulate falling
            rock, bottom = simulate_step(rock, board, wind[wind_step%len(wind)])
            wind_step+=1
            if bottom:
                board.update(rock)
                break
    return max([i for i,j in board])+1

def simulate_reps(nrocks, wind):
    board = set()
    wind_step = 0
    prev_height = -1
    output = []
    for rnum in range(nrocks):
        # get init rock
        # get tallest rock - 3 away
        height = -1 if not len(board) else max([i for i,j in board])
        # origin = (tallest rock + 4, 2)
        origin = (height + 4, 2)
        # get rock
        rock = get_rock(origin, rnum%5)
        while True:
            # simulate falling
            rock, bottom = simulate_step(rock, board, wind[wind_step%len(wind)])
            wind_step+=1
            if bottom:
                board.update(rock)
                break
        new_h = max(rock)
        output.append((new_h[0]-prev_height, new_h[1], wind_step%len(wind)))
        prev_height = new_h[0]
    return output


# def main(data_file):
#     hend = 1000000000000
#     data = parse_input(data_file)
#     coords = simulate_reps(2000, data)
#     # get subsets to indices
#     subsets_to_idx = defaultdict(list)
#     for idx,_ in enumerate(coords[:-40]):
#         subsets_to_idx[tuple(coords[idx:idx+40])].append(idx)
#     subsets_to_form = defaultdict(list)
    
#     # get mx+b form
#     for subset, indices in subsets_to_idx.items():
#         diff = None
#         for i,idx in enumerate(indices[1:]):
#             if diff is not None:
#                 assert diff == idx-indices[i]
#             diff = idx-indices[i]
#         if not diff is None:
#             subsets_to_form[subset] = [indices[0], diff]
    
#     for subset, form in subsets_to_form.items():
#         heiend = hend+1
#         if (heiend-form[0])%form[1] == 0:
#             val = (heiend-form[0])/form[1]-1
#             break
#     b = simulate(form[0]+1, data)
#     cyc_h = simulate(sum(form)+1, data)
#     print(subset,subsets_to_idx[subset])
#     return int(val*(cyc_h-b)+b)

ROCKS = [
    (0,1j,2j,3j),
    (1,1j,1+1j,2+1j,1+2j),
    (0,1j,2j,1+2j,2+2j),
    (0,1,2,3),
    (0,1j,1,1+1j)
]

def check_valid(point: complex, stack: set[complex]):
    return point not in stack and point.imag in range(7) and point.real > 0

def check_valid_rock(origin:complex, rock_type:int, stack:set[complex]):
    return all([check_valid(x+origin, stack) for x in ROCKS[rock_type]])

CYCLE_STOP = 1000000000000

def main(data_file):
    wind = parse_input(data_file)
    NUM_ACCUM = len(wind)
    stack = set()
    top = 0
    prev_top = 0
    wind_num = 0
    cycles = {}
    accum = []
    rtype = -1
    for nrock in range(100000):
        # calculations
        if nrock == 2022:
            print(int(top))

        # if cycle detected
        # get cycle key
        accum.append((rtype, int(top-prev_top)))
        if len(accum) > NUM_ACCUM:
            accum.pop(0)
            key = tuple(accum)
            if not key in cycles:
                cycles[key] = [nrock, top]
            else:
                num_cyc, remain = divmod(CYCLE_STOP-nrock, nrock - cycles[key][0])
                if not remain:
                    return num_cyc*(top - cycles[key][1])+top

        # process rocks
        ## simulate falling rock
        pos = complex(4+top,2)
        rtype = nrock%len(ROCKS)
        while True:
            smov = -1j if wind[wind_num%len(wind)] == "<" else 1j
            # move side
            if check_valid_rock(pos+smov, rtype, stack): pos = pos+smov
            wind_num+=1
            # move down
            if check_valid_rock(pos-1, rtype, stack):
                pos = pos-1
            else:
                # exit if can't move down.
                break
        ## add to stack
        stack = stack | set([pos+i for i in ROCKS[rtype]])
        # Get top of stack
        prev_top = top
        top = max(stack, key=lambda x: x.real).real



SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_17.t')
    eout = 1514285714288
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_17')
    print("Main out", mout)
