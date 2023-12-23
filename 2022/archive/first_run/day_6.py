import os
from collections import defaultdict

def main(data_file):
    with open(data_file) as f:
        lines = f.readlines()
    code = lines[0]
    rset = {}
    for idx,char in enumerate(code):
        if char in rset:
            popval = rset[char]
            rset = {k:v for k,v in rset.items() if popval < v}
        rset[char] = idx
        if len(rset) == 14:
            break
    return idx+1

if __name__ == "__main__":
    print("****** Test Data *******")
    print(main('test_log_6.txt'))
    print("****** Real Data *******")
    print(main('log_6.txt'))

