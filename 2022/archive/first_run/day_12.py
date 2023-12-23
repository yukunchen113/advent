"""
u,d,l,r

at most 1 higher
m -> n 
m -/-> o

get fewest possible steps required from S -> E, S == a, E == z
"""
from collections import defaultdict


def find_letter(letter: str, matrix: list[list[str]], is_first: bool = True) -> tuple[int, int]:
    all_letters = []
    for ridx, row in enumerate(matrix):
        for cidx, ele in enumerate(row):
            if ele == letter:
                coord = (ridx, cidx)
                all_letters.append((ridx, cidx))
                if is_first:
                    return coord
    if not is_first:
        return all_letters
    raise Exception(f"Not found '{letter}'")


def parse_matrix(data_file: str) -> list[list[str]]:
    matrix = []
    with open(data_file) as f:
        for line in f.readlines():
            if line:
                matrix.append(list(line.strip()))
    return matrix


def is_invalid(coord: str, ncoord: str) -> bool:
    cur = ord(coord)
    new = ord(ncoord)
    return (new - cur) > 1


def find_score(matrix, start, final):
    stack = [start]
    matrix[final[0]][final[1]] = "z"
    matrix[start[0]][start[1]] = "a"
    nlayer = 0
    score = {}
    while stack:
        new_stack = []
        for coord in stack:
            if coord in score:
                continue
            cletter = matrix[coord[0]][coord[1]]
            score[coord] = nlayer
            for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ridx, cidx = coord[0]+i, coord[1]+j
                new_coord = (ridx, cidx)
                if ridx == -1 or cidx == -1 or ridx == len(matrix) or cidx == len(matrix[0]) or is_invalid(cletter, matrix[ridx][cidx]):
                    continue
                new_stack.append(new_coord)
        stack = new_stack
        nlayer += 1
    if not final in score:
        return float("inf")
    return score[final]


def main(data_file):
    matrix = parse_matrix(data_file)
    start = find_letter("S", matrix)
    all_letters = [start] + find_letter("a", matrix, False)
    final = find_letter("E", matrix)
    return min([find_score(matrix, start, final) for start in all_letters])


if __name__ == "__main__":
    print(main("data_12"))
    assert main("data_12.t") == 29
