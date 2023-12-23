import os
from collections import defaultdict

def interpolate(x,y):
    x,y = max(x,y), min(x,y)
    data = []
    for i in range(x[0]-y[0]):
        data.append((y[0]+i, y[1]))
    for j in range(x[1]-y[1]):
        data.append((y[0], y[1]+j))
    return data

def parse_line(line):
    line = list(line.replace(" -> ", "-")+"-")
    data = []
    num = ""
    coord = []
    while line:
        char = line.pop(0)
        if char == ",":
            coord.append(int(num))
            num = ""
        elif char == "-":
            coord.append(int(num))
            num = ""
            data.append(tuple(coord))
            # add interpolations
            if len(data) > 1:
                data = interpolate(data[-1], data[-2]) + data
            coord = []
        else:
            num+=char
    return set(data)

def parse_input(data_file):
    """store into set of coordinates with rocks"""
    data = set()
    with open(data_file) as f:
        lines = f.readlines()
        for line in lines:
            data = data | parse_line(line)
    return data

def strav(coord, data, lowest):
    # # return "free" if free flow
    # if check_stop_cond(coord):
    #     return coord
    # return coord if settled
    if coord in data or check_hit_bottom(coord, lowest):
        return None
    # go down
    new_coord = (coord[0], coord[1]+1)
    if not new_coord in data:
        return strav(new_coord, data, lowest) or coord
    # go left
    new_coord = (coord[0]-1, coord[1]+1)
    if not new_coord in data:
        return strav(new_coord, data, lowest) or coord
    # go right
    new_coord = (coord[0]+1, coord[1]+1)
    if not new_coord in data:
        return strav(new_coord, data, lowest) or coord
    # no where to go
    return coord

def get_final_sand_position(data, lowest):
    start = (500, 0)
    coord = strav(start, data, lowest) 
    if check_stop_cond(coord):
        return coord
    else:
        return coord


def main(data_file):
    data = parse_input(data_file)
    coord = True
    lowest = max([i for _,i in data])
    pile = 0
    while not check_stop_cond(coord):
        coord = get_final_sand_position(data, lowest)
        data.add(coord)
        pile += 1
    return pile


def check_hit_bottom(coord,ll):
    return coord[1] == ll+2


def check_stop_cond(coord):
    return coord == (500,0)


def check_free_flow(coord, data):
    """
    Detect freeflow given input

    metric (any): 
    - Once it gets past (or equal) the lowest line of rocks, it's gone.
    - once it gets past (or equal) the left most rock, it's gone
    """
    lowest_line = max([i for _,i in data])
    leftmost_line = min([i for i,_ in data])
    return coord[0] <= leftmost_line or coord[1] >= lowest_line



SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_14.t')
    print(tout)
    assert tout == 93, tout
    print(main("data_14"))
    # print("****** Test Log *******")
    # if SHOW_MAIN:
    #     print("****** Main Log *******")
    #     mout = main('data_14')
    # print("****** Test Data *******")
    # print(tout, "answer")
    # if SHOW_MAIN:
    #     print("****** Real Data *******")
    #     print(mout)
