import os
from collections import defaultdict


def parse_input(data_file) -> list[tuple[int, int, int]]:
    with open(data_file) as f:
        lines = f.readlines()
    return [tuple(float(i) for i in line.split(",")) for line in lines]


CUBE_FACES = [
    (0.5, 0, 0),
    (-0.5, 0, 0),
    (0, 0.5, 0),
    (0, -0.5, 0),
    (0, 0, 0.5),
    (0, 0, -0.5),
]


def get_cube_faces(cubes):
    open_faces = set()
    for cube in cubes:
        for face in CUBE_FACES:
            face = tuple(x+y for x, y in zip(cube, face))
            if face in open_faces:
                open_faces.remove(face)
            else:
                open_faces.add(face)
    return open_faces


def get_surround(cur_cubes):
    # get min x cube, use x-1 as starting
    starting_coord = list(min(cur_cubes))
    starting_coord[0] -= 1
    starting_coord = tuple(starting_coord)

    # traverse, at most 1 away (in any direction) from any given cube, can't traverse to existing cubes
    new_cubes = set()
    level = [starting_coord]
    while level:
        new_level = []
        for coord in level:
            if coord in cur_cubes:
                continue
            # get min diff for all cubes
            minimums = [float("inf")]*3
            for cube in cur_cubes:
                for idx in range(3):
                    minimums[idx] = min(minimums[idx],abs(coord[idx]-cube[idx]))
            if max(minimums) > 1:
                continue
            if coord in new_cubes:
                continue
            new_cubes.add(coord)
            for idx in range(3):
                for sign in [1,-1]:
                    new_coord = list(coord)
                    new_coord[idx] += sign
                    new_level.append(tuple(new_coord))
        level = new_level
    return new_cubes

def main(data_file):
    cubes=parse_input(data_file)
    return len(get_cube_faces(cubes) & get_cube_faces(get_surround(cubes)))


SHOW_MAIN=0
if __name__ == "__main__":
    tout=main('data_18.t')
    eout=58
    assert tout == eout, tout
    print("Test Success")
    mout=main('data_18')
    print("main: ", mout)
