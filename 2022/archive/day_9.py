TEST_DATA_FILE = "data_9.t"
DATA_FILE = "data_9"

MOVEMENT = {"U":(-1,0), "D":(1,0), "R":(0,1), "L":(0,-1)}

def move_head(head_pos, direc):
    # returns new head position
    return head_pos[0] + MOVEMENT[direc][0], head_pos[1] + MOVEMENT[direc][1]

def move_link(tail_pos, head_pos):
    new_tail_pos = list(tail_pos)
    # move if head more than one along either x or y axis.
    ydiff = head_pos[0] - tail_pos[0]
    xdiff = head_pos[1] - tail_pos[1]
    move = abs(ydiff) > 1 or abs(xdiff) > 1
    if move and ydiff:
        new_tail_pos[0] += ydiff/abs(ydiff)
    if move and xdiff:
        new_tail_pos[1] += xdiff/abs(xdiff)
    return tuple(new_tail_pos)

def run_instructions(instructions):
    rope_pos = [(0,0) for _ in range(10)]
    tail_visit = set([(0,0)])
    for instruction in instructions:
        direc, num = instruction.split()
        for _ in range(int(num)):
            for idx, pos in enumerate(rope_pos):
                if not idx:
                    rope_pos[idx] = move_head(pos, direc)
                else:
                    rope_pos[idx] = move_link(rope_pos[idx], rope_pos[idx-1])
            tail_visit.add(rope_pos[-1])
    return len(tail_visit)

if __name__ == "__main__":
    # load data
    with open(DATA_FILE) as f:
        instructions = f.readlines()
    print(run_instructions(instructions))