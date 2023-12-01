import os
from collections import defaultdict
import numpy as np

def get_op_params(line):
    if "+" in line:
        op_params = [int(line.split()[-1]),1,1]
    elif "* old" in line:
        op_params = [0,1,2]
    elif "*" in line:
        op_params = [0,int(line.split()[-1]),1]
    else:
        raise ValueError("unknown op")
    return op_params

def process_monkeys(lines):
    monkey_data = []
    itemset = []
    for line in lines:
        line:str
        if line.startswith("Monkey"):
            monkey_data.append({"throw":[None, None]})
        elif line.startswith("  Starting items: "):
            itemset.append([int(item) for item in line.replace("  Starting items: ", "").split(", ")])
        elif line.startswith("  Operation: "):
            line = line.replace("  Operation: new = ", "")
            monkey_data[-1]["operation"] = get_op_params(line)
        elif line.startswith("  Test: divisible by "):
            line = line.replace("  Test: divisible by ", "")
            monkey_data[-1]["test"] = int(line)
        elif line.startswith("    If true: throw to monkey "):
            line = line.replace("    If true: throw to monkey ", "")
            monkey_data[-1]["throw"][1] = int(line)
        elif line.startswith("    If false: throw to monkey "):
            line = line.replace("    If false: throw to monkey ", "")
            monkey_data[-1]["throw"][0] = int(line)
    return itemset, monkey_data

def process_monkey(items, throw, test, operation, prod):
    new_monkeys = defaultdict(lambda: [])
    for item in items:
        # print("start")
        params = operation
        #print(operation)
        # print("start")
        new_item = (((item**params[2])+params[0])*params[1])%prod
        # print("op")
        new_monkeys[throw[int(not new_item%test)]].append(new_item)
        # print("itemset")
    return new_monkeys

def main(data_file):
    with open(data_file) as f:
        lines = f.readlines()
    inspections = defaultdict(lambda: 0)
    itemset, monkey_data = process_monkeys(lines)
    prod = np.prod([i["test"] for i in monkey_data])
    for idx in range(10000):
        print(f"\r cycle{idx}", end="")
        for mnum,items in enumerate(itemset):
            inspections[mnum] += len(items)
            new_monkeys = process_monkey(items, monkey_data[mnum]["throw"], monkey_data[mnum]["test"], monkey_data[mnum]["operation"], prod)
            for k,v in new_monkeys.items():
                itemset[k] += v
            itemset[mnum] = []
            if idx+1 in [1,20]+ [i*1000 for i in range(1,11)]:
                print(dict(inspections), dict(new_monkeys))
    inspections = sorted(inspections.values())
    return inspections[-1]*inspections[-2]


if __name__ == "__main__":
    show_main = 1
    print("****** Test Log *******")
    tout = main('data_11.t')
    if show_main:
        print("****** Main Log *******")
        mout = main('data_11')
    print("****** Test Data *******")
    print(tout, "answer")
    if show_main:
        print("****** Real Data *******")
        print(mout)
    