import os
from collections import defaultdict


def parse_input(data_file):
    with open(data_file) as f:
        lines = f.readlines()
    return [int(i.replace("\n", "")) for i in lines]

def swap(data, idx, nsteps, direction):
    # swap val at idx for nsteps times
    for _ in range(nsteps):
        nidx = (idx+direction)%len(data)
        data[idx],data[nidx] = data[nidx],data[idx]
        idx = nidx
    return data

def main(data_file):
    data = parse_input(data_file)
    data = list([(i,j*811589153) for i,j in enumerate(data)])
    for key in data.copy()*10:
        idx = data.index(key)
        _,val = key
        # process val
        if val:
            dir = val//abs(val)
            val = (abs(val)%(len(data)-1))
        if val:
            data = swap(data, idx, val, dir)
    # process
    data = [i[1] for i in data]
    zidx = data.index(0)
    return sum(data[(zidx+i)%len(data)] for i in [1000, 2000, 3000])

SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_20.t')
    eout = 1623178306
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_20')
    print("main: ", mout)
