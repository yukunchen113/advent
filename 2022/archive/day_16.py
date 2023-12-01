import os
import re
from collections import defaultdict


def parse_input(data_file):
    data = {}
    with open(data_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n")
            data[line[6:8]] = (int(re.findall(r'[-+]?\d+', line)[0]),
                               line.split(";")[1].strip(" tunnels lead to valves ").split(", "))
    return data


class Trav():

    MAX_TIME = 26

    def __init__(self):
        self.memo = {}
        self.aop = set()

    def __call__(self, pos, minu, n_helpers, data):
        if minu > self.MAX_TIME:
            return 0 if n_helpers == 0 else self("AA", 1, n_helpers-1, data)
        if (pos, minu, n_helpers, tuple(sorted(list(self.aop)))) in self.memo:
            return self.memo[(pos, minu, n_helpers, tuple(sorted(list(self.aop))))]
        max_val = -float("inf")
        for mode in data[pos]:  # can be val, path
            is_open = False
            if isinstance(mode, int):
                paths = [pos]
                if not pos in self.aop:
                    add = mode*(self.MAX_TIME-minu)
                    is_open = True
                    if add <= 0:
                        continue
                else:
                    continue
            else:
                paths = mode
                add = 0
            for npos in paths:
                if is_open:
                    self.aop.add(pos)
                val = add + self(npos, minu+1, n_helpers, data)
                if is_open:
                    self.aop.remove(pos)
                max_val = max(val, max_val)
        self.memo[(pos, minu, n_helpers, tuple(
            sorted(list(self.aop))))] = max_val
        return max_val


def main(data_file):
    data = parse_input(data_file)  # data should be: (val, [path, path, ...])
    trav = Trav()
    return trav("AA", 1, 1, data)


SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_16.t')
    eout = 1707
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_16')
    print(mout)
