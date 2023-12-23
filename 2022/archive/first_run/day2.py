with open("inp2.txt") as f:
    lines = f.readlines()

wlht = {
    "A":{"X":3, "Y":1, "Z":2},
    "B":{"X":1, "Y":2, "Z":3},
    "C":{"X":2, "Y":3, "Z":1}
}
types = {"X":0, "Y":3, "Z":6}
score = 0
for line in lines:
    o,y = line.split()
    score += types[y] + wlht[o][y]
print(score)
    