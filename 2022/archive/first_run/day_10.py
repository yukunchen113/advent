import os
from collections import defaultdict

def main(data_file):
    with open(data_file) as f:
        lines = f.readlines()

    imp_cycles = [(i+1)*40 for i in range(6)]
    draw = ""
    regis = 1
    tim = 1
    for line in lines:
        draw += pixel(tim, regis) # during the current cycle
        if line.startswith("addx"):
            val = int(line.split()[1])
            if tim in imp_cycles: # after the current stage
                draw += "\n"
            tim += 1 # middle stage increment
            draw += pixel(tim, regis) # during the new stage
            tim += 1
            regis += val
        else:
            tim += 1
        if tim-1 in imp_cycles: # after the current stage
            draw += "\n"
    return draw

def pixel(cycle, x):
    if (cycle-1)%40 in [x-1, x, x+1]:
        return "#"
    else:
        return "."
        

if __name__ == "__main__":
    show_main = 1
    print("****** Test Log *******")
    tout = main('data_10.t')
    if show_main:
        print("****** Main Log *******")
        mout = main('data_10')
    print("****** Test Data *******")
    print(tout, "answer")
    if show_main:
        print("****** Real Data *******")
        print(mout)
    