import os
from collections import defaultdict

def mark_visible_lr(array):
    # returns num visible, idx of last visible tree
    maxh, narr = -1, []
    for val in array:
        if val > maxh:
            maxh = val
            val = -2
        narr.append(val)
    return narr
    
def mark_visible_arr(array):
    narr = mark_visible_lr(array)
    narr2 = reversed(mark_visible_lr(reversed(array)))
    return [min(i,j) for i,j in zip(narr, narr2)]

def transpose(matrix):
    new_mat = [[0]*len(matrix) for _ in range(len(matrix[0]))]
    for i,row in enumerate(matrix):
        for j,ele in enumerate(row):
            new_mat[j][i] = ele
    return new_mat

def min_mat(matrix1, matrix2):
    new_mat = []
    for r1,r2 in zip(matrix1,matrix2):
        new_mat.append([min(i,j) for i,j in zip(r1,r2)])
    return new_mat

def mark_visible_matrix(matrix):
    row_visible = [mark_visible_arr(row) for row in matrix]
    col_visible = transpose([mark_visible_arr(row) for row in transpose(matrix)])
    return min_mat(row_visible, col_visible)

def check_scenic_direction(val, arr):
    nvis = 0
    for i in arr:
        nvis += 1
        if i >= val: break
    return nvis

def get_scenic_score(coord, matrix):
    idx,jdx = coord
    val = matrix[idx][jdx]
    row, col = matrix[idx], [row[jdx] for row in matrix] # going downwards
    score = check_scenic_direction(val, row[jdx+1:])
    score *= check_scenic_direction(val, reversed(row[:jdx]))
    score *= check_scenic_direction(val, col[idx+1:])
    score *= check_scenic_direction(val, reversed(col[:idx]))
    return score

def main(data_file):
    with open(data_file) as f:
        lines = f.readlines()
    # check increasing items for each edge.
    data = []
    for line in lines:
        data.append([int(i) for i in line.strip("\n")])
    
    # visible = mark_visible_matrix(data)
    max_score = -1
    for i,row in enumerate(data):
        for j,ele in enumerate(row):
            score = get_scenic_score((i,j),data)
            max_score = max(score, max_score)
    return max_score
    

if __name__ == "__main__":
    print("****** Test Log *******")
    tout = main('data_8.t')
    print("****** Main Log *******")
    mout = main('data_8')
    print("****** Test Data *******")
    print(tout)
    print("****** Real Data *******")
    print(mout)
    