import os
from collections import defaultdict


def parse_input(data_file):
    elf_pos = set()
    with open(data_file) as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
        for ridx, row in enumerate(lines):
            for cidx, ele in enumerate(row):
                if ele == "#":
                    elf_pos.add(complex(ridx, cidx))
    return elf_pos


def is_valid(elf, dir, elvespos):
    for square in dir:
        if (elf + square) in elvespos:
            return False
    return True


def main(data_file):
    dirpop = [
        [-1, -1-1j, -1+1j],
        [1, 1-1j, 1+1j],
        [-1j, -1-1j, 1-1j],
        [1j, -1+1j, 1+1j],
    ]
    elvespos = parse_input(data_file)
    step = 1
    while True:
        proposal = {}
        for elf in elvespos:
            valdir = [is_valid(elf, dir, elvespos) for dir in dirpop]
            if all(valdir) or not any(valdir):
                continue
            newelf = elf+dirpop[valdir.index(True)][0]
            if newelf in proposal:
                proposal[newelf] = None
            else:
                proposal[newelf] = elf
        if all([i is None for i in proposal.values()]):
            return step
        for newelf, oldelf in proposal.items():
            if oldelf is not None:
                elvespos.remove(oldelf)
                elvespos.add(newelf)
        dirpop.append(dirpop.pop(0))
        step += 1
    # noso = [i.real for i in elvespos]
    # eawe = [i.imag for i in elvespos]
    # return (max(noso)-min(noso)+1)*(max(eawe)-min(eawe)+1)-len(elvespos)


SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_23.t')
    eout = 20
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_23.m')
    print("main: ", mout)
