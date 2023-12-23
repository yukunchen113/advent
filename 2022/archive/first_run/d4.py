with open("l4") as f:
    pairs = f.readlines()
nass = 0
for pair in pairs:
    f,s = pair.split(",")
    f = [int(i) for i in f.split("-")]
    s = [int(i) for i in s.split("-")]
    pair = sorted([f,s])
    if pair[1][0] <= pair[0][1]:
        print(pair)
        nass +=1
print(nass)