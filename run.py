import os
from collections import defaultdict
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np

def parse_input(data_file):
    with open(data_file) as f:
        lines = [i.replace("\n", "") for i in f.readlines()]
    return lines

def main(data_file):
    data = parse_input(data_file)

if __name__ == "__main__":
    tout = main('data_3.t')
    eout = 
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_3.m')
    print("main: ", mout)
