import os
from collections import defaultdict, Counter
import regex as re
from pprint import pprint
from functools import reduce
import numpy as np
from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=198)
def pt1(data_file):
    data = [[int(j) for j in i.strip()] for i in open(data_file).readlines()]
    nones = np.sum(data, axis=0)
    nzeros = len(data) - nones
    gamma = ''.join([str(int(i>j)) for i,j in zip(nones, nzeros)])
    eps = ''.join([str(int(i<j)) for i,j in zip(nones, nzeros)])
    return int(gamma, 2)*int(eps, 2)

@mark.solution(test=230)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    ogr = ""
    for idx in range(len(data[0])):
        matches = [i for i in data if i.startswith(ogr)]
        if len(matches) == 1:
            ogr = matches[0]
            break
        matches = [int(i[idx]) for i in matches]
        ogr += str(int(len(matches) - sum(matches) <= sum(matches)))
    csr = ""
    for idx in range(len(data[0])):
        matches = [i for i in data if i.startswith(csr)]
        if len(matches) == 1:
            csr = matches[0]
            break
        matches = [int(i[idx]) for i in matches]
        csr += str(int(not (len(matches) - sum(matches) <= sum(matches))))
    return int(ogr, 2)*int(csr, 2)
    