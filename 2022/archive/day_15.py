import os
import re
from collections import defaultdict


def parse_input(data_file):
    with open(data_file) as f:
        lines = f.readlines()
        output = {}
        for line in lines:
            nums = re.findall(r'[-+]?\d+', line)
            output[(int(nums[0]), int(nums[1]))] = (int(nums[2]), int(nums[3]))
    return output


def get_coords_checked_interval(nrow: int, scoord, dist) -> set[tuple[int, int]]:
    ydiff = abs(scoord[1] - nrow)
    int_set = set()
    if ydiff <= dist:
        int_set.add((scoord[0], scoord[0]))
        side_len = dist - ydiff
        int_set.add((scoord[0]-side_len, scoord[0]+side_len))
    return int_set


def get_dist(scoord, bcoord):
    return abs(scoord[0] - bcoord[0]) + abs(scoord[1] - bcoord[1])

# tbounds: 0 -20
# bounds: 0 - 4000000
# coord[0]*4000000+coord[1]


def get_row_diff(data, nrow, max_xy):
    interval_set = set()
    for scoord, bcoord in data.items():
        dist = get_dist(scoord, bcoord)
        interval_set = interval_set | get_coords_checked_interval(
            nrow, scoord, dist)
    intervals = sorted(list(interval_set))
    max_end = -float("inf")
    for intv1, intv2 in zip(intervals[:-1], intervals[1:]):
        # check for gap, and if gap is between 0, max_xy inclusive
        max_end = max(intv1[1], max_end)
        if max_end < intv2[0] - 1:
            gap = intv2[0] - 1
            if 0 <= gap and gap <= max_xy:
                return gap
    return None


def main(data_file, max_xy):
    data = parse_input(data_file)
    for nrow in range(max_xy+1):
        gap = get_row_diff(data, nrow, max_xy)
        if gap is not None:
            return gap*4000000+nrow
    raise Exception("Invalid file")


SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_15.t', 20)
    eout = 56000011
    assert tout == eout, tout
    mout = main('data_15', 4000000)
    print(mout)
