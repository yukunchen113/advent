import os
from collections import defaultdict
import math
from typing import Union

def parse_input(data_file):
    with open(data_file) as f:
        lines = [i.replace("\n", "") for i in f.readlines()]
    return lines

def snafu_to_dec(snafu:Union[list[int], str])->int:
    num = 0
    for idx, char in enumerate(snafu):
        if char == "-":
            dig = -1
        elif char == "=":
            dig = -2
        else:
            dig = int(char)
        num+=dig*5**(len(snafu)-1-idx)
    return num

def dec_to_snafu(dec:int)->str:
    # get first digit, with dec
    digits = [2]
    while dec > snafu_to_dec(digits):
        digits = [2] + digits
    for idx in range(len(digits)):
        if idx: digits[idx] = 0
            
    for idx in range(len(digits)):
        new_digits = digits.copy()
        min_diff, min_val = float("inf"), 0
        for val in range(-2,3):
            new_digits[idx] = val
            diff = abs(dec - snafu_to_dec(new_digits))
            if min_diff > diff:
                min_diff = diff
                min_val = val
            print(new_digits, diff)
        digits[idx] = min_val
    # convert digits
    return "".join([str(i) if i >= 0 else ["=", "-"][i] for i in digits])
        
        
    
    

def main(data_file):
    data = parse_input(data_file)
    num = sum(snafu_to_dec(i) for i in data)
    return dec_to_snafu(num)

SHOW_MAIN = 0
if __name__ == "__main__":
    tout = main('data_25.t')
    eout = "2=-1=0"
    assert tout == eout, tout
    print("Test Success")
    mout = main('data_25.m')
    print("main: ", mout)
