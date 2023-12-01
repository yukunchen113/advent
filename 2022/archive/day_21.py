import os
from collections import defaultdict
import re


def parse_input(data_file):
    with open(data_file) as f:
        lines = f.readlines()
        output = {}
        for line in lines:
            match = re.findall(
                f"(....): (\d+)?(?:(....) (.) (....))?", line)[0]
            if match[1]:
                output[match[0]] = int(match[1])
            else:
                output[match[0]] = match[2:]
    return output


def get_num(key, data):
    if isinstance(data[key], int):
        return data[key]
    m1, op, m2 = data[key]
    m1, m2 = get_num(m1, data), get_num(m2, data)
    if op == "+":
        output = m1 + m2
    elif op == "-":
        output = m1 - m2
    elif op == "/":
        output = m1 / m2
    elif op == "*":
        output = m1 * m2
    return output


def get_eq(key, data):
    if key == "humn":
        return [1, 0]
    if isinstance(data[key], int):
        return [0, data[key]]

    m1, op, m2 = data[key]

    a, b = get_eq(m1, data)
    c, d = get_eq(m2, data)
    assert not a or not c, "circular :("
    if op == "+":
        output = [a+c, b+d]
    elif op == "-":
        output = [a-c, b-d]
    elif op == "/":
        if not a and not c:
            output = [0, b/d]
        else:
            output = [a/d or b/c, b/d]
    elif op == "*":
        output = [a*d+b*c, b*d]
    return output


def main(data_file):
    data = parse_input(data_file)
    m1, _, m2 = data["root"]
    a, b = get_eq(m1, data)
    d, c = get_eq(m2, data)
    return (c-b)/(a-d)


SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_21.t')
    eout = 301
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_21')
    print("main: ", mout)
