from collections import defaultdict

def create_stacks(yard):
    # returns dict of list
    stacks = defaultdict(lambda: [])
    for line in yard:
        for idx, val in enumerate(range(1,len(line),4),1):
            if line[val-1] == "[":
                stacks[idx].append(line[val])
    stacks = {k:list(reversed(v)) for k,v in stacks.items()}
    return stacks

def main():
    with open("l5") as f:
        data = f.readlines()
    yard = []
    moves = []
    for line in data:
        if "move" in line:
            move = line.split(" ")
            moves.append([int(move[1]), int(move[3]), int(move[-1])])
        elif not line == "\n":
            yard.append(line)
    yard = create_stacks(yard)
    for nb, fy, ty in moves:
        yard[ty] += yard[fy][-nb:]
        yard[fy] = yard[fy][:-nb]
    return "".join([yard[i+1][-1] for i in range(len(yard))])

print(main())
