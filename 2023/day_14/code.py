from advent import mark
from advent.tools.map import convert_to_complex

@mark.solution(test=136)
def pt1(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    length = len(data)
    data = convert_to_complex(data)
    srocks = set(i for i,v in data.items() if v =="#")
    rrocks = set(i for i,v in data.items() if v =="O")
    change = True
    while change:
        nrrocks = set()
        change = False
        for rrock in rrocks:
            if (rrock-1) in data and (rrock-1) not in srocks and (rrock-1) not in nrrocks:
                nrrocks.add(rrock-1)
                change = True
            else:
                nrrocks.add(rrock)
        rrocks = nrrocks
    return int(sum(length-rrock.real for rrock in rrocks))

def sort_direction(dir, x):
    if dir == -1:
        return x.real
    if dir == -1j:
        return x.imag
    if dir == 1:
        return -x.real
    if dir == 1j:
        return -x.imag

@mark.solution(test=64)
def pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    length = len(data)
    data = convert_to_complex(data)
    srocks = set(i for i,v in data.items() if v =="#")
    rrocks = set(i for i,v in data.items() if v =="O")
            
    store = {}
    output = -1
    for step in range(1000000001):
        config = tuple(sorted((i.real, i.imag) for i in rrocks))
        if config in store:
            _,r = divmod(1000000000 - store[config], step - store[config])
            if not r:
                return output
        store[config] = step
        
        for dir in [-1,-1j,1,1j]:
            change = True
            while change:
                nrrocks = set()
                change = False
                for rrock in sorted(list(rrocks), key = lambda x: sort_direction(dir, x)):
                    if (rrock+dir) in data and (rrock+dir) not in srocks and (rrock+dir) not in nrrocks:
                        nrrocks.add(rrock+dir)
                        change = True
                    else:
                        nrrocks.add(rrock)
                rrocks = nrrocks
        output = int(sum(length-rrock.real for rrock in rrocks))

    return output


@mark.solution(test=64)
def cleaner_pt2(data_file):
    data = [i.strip() for i in open(data_file).readlines()]
    length = len(data)
    data = convert_to_complex(data)
    rrocks = set(i for i,v in data.items() if v =="O")
            
    store = {}
    for step in range(1000000001):
        config = tuple(sorted((i.real, i.imag) for i in rrocks))
        if config in store and not (1000000000 - store[config])%(step - store[config]):
            return output
        store[config] = step
        
        for dir in [-1,-1j,1,1j]:
            change = True
            while change:
                nrrocks, change = set(), False
                for rrock in sorted(list(rrocks), key = lambda x: sort_direction(dir, x)):
                    if data.get(rrock+dir, "#") != "#" and (rrock+dir) not in nrrocks:
                        nrrocks.add(rrock+dir)
                        change = True
                    else:
                        nrrocks.add(rrock)
                rrocks = nrrocks
        output = int(sum(length-rrock.real for rrock in rrocks))

    return output