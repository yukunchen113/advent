from collections import defaultdict
def get_freqs(comp):
    freqs = defaultdict(lambda: 0)
    for i in comp: freqs[i] += 1
    return freqs

def get_priority(letter):
    if ord(letter) >= ord("a"):
        return ord(letter) - ord("a") + 1
    elif ord(letter) >= ord("A"):
        return ord(letter) - ord("A") + 27
    else:
        return 0

with open("i3.txt") as f:
    lines = f.readlines()
score = 0
ln = []
for sack in lines:
    ln.append(set(sack))
    if len(ln) == 3:
        for k in ln[0]:
            score += get_priority(k) if k in ln[0] and k in ln[1] and k in ln[2] else 0
        ln = []
print(score)
