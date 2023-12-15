from collections import defaultdict
from advent import mark

@mark.solution(test=1320)
def pt1(data_file):
    data = [i.replace("\n", "") for i in open(data_file).readlines()][0].split(",")
    total = 0
    for seq in data:
        val = 0
        for c in seq:
            val = ((val+ord(c))*17)%256
        total += val
    return total

def get_hash(string):
    val = 0
    for c in string:
        val = ((val+ord(c))*17)%256
    return val

@mark.solution(test=145)
def pt2(data_file):
    data = [i.replace("\n", "") for i in open(data_file).readlines()][0].split(",")
    total = 0
    storage = defaultdict(dict)
    for seq in data:
        if seq.endswith("-"):
            storage[get_hash(seq[:-1])].pop(seq[:-1], None)
        elif "=" in seq:
            label, val = seq.split("=")
            storage[get_hash(label)][label] = val
    total = 0
    for nbox,box in storage.items():
        for slot, (_, fl) in enumerate(box.items(),1):
            total+=(nbox+1)*slot*int(fl)
    return total