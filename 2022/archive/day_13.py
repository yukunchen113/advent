import os
from collections import defaultdict

TEST_FILE = "data_13.t"
FILE = "data_13"


def parse_line(idx_str):
    idx_str = idx_str[1:]
    idx_list = []
    cur_num = ""
    cur_list = None
    while idx_str:
        char = idx_str[0]
        if char == "[":
            idx_str, cur_list = parse_line(idx_str)
        elif char == "," or char == "]":
            if cur_num:
                idx_list.append(int(cur_num))
            if cur_list is not None:
                idx_list.append(cur_list)
            if char == "]":
                return idx_str, idx_list
            cur_num = ""
            cur_list = None
        else:
            cur_num += char
        idx_str = idx_str[1:]


def parse_df(data_file: str):
    with open(data_file) as f:
        lines = f.readlines()
    pairs = [[]]
    for line in lines:
        line = line.strip()
        if line == "":
            pairs.append([])
        else:
            _, line = parse_line(line)
            pairs[-1].append(line)
    return pairs


def compair(a, b) -> bool:
    if type(a) != type(b):
        if isinstance(a, list):
            return compair(a, [b])
        else:
            return compair([a], b)
    if isinstance(a, int):
        if a == b:
            return None
        return a < b
    for idx in range(max(len(a), len(b))):
        if idx >= len(a):
            return True
        elif idx >= len(b):
            return False
        elif a[idx] == b[idx]:
            pass
        else:
            out = compair(a[idx], b[idx])
            if compair(a[idx], b[idx]) is not None:
                return out


def mergesort(packets) -> list:
    if not len(packets) or len(packets) == 1:
        return packets
    a = mergesort(packets[:len(packets)//2])
    b = mergesort(packets[len(packets)//2:])
    new = []
    while a or b:
        if not a:
            new.append(b.pop(0))
        elif not b:
            new.append(a.pop(0))
        else:
            # print(a[0], b[0], compair(a[0], b[0]))
            if compair(a[0], b[0]):
                new.append(a.pop(0))
            else:
                new.append(b.pop(0))
    return new


def main(data_file):
    pairs = parse_df(data_file)
    new_pairs = []
    for pair in pairs:
        new_pairs += pair
    new_pairs += [[[2]], [[6]]]
    new_pairs = mergesort(new_pairs)
    return (new_pairs.index([[2]]) + 1) * (new_pairs.index([[6]]) + 1)
    # return total


if __name__ == "__main__":
    print(main(TEST_FILE))
    # assert main(TEST_FILE) == 13
    out = main(FILE)
    print(out)
