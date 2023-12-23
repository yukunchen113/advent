import heapq

top3 = [-float("inf")]*3
elf = 0
with open("inputd1.txt") as f:
    lines = f.readlines()
for line in lines:
    if line == "\n":
        # each elf:
        if top3[0] < elf:
            heapq.heappop(top3)
            heapq.heappush(top3, elf)

        # next elf:
        elf = 0
    else:
        elf += int(line)
print(sum(top3))