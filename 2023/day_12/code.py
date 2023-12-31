from functools import cache
from advent import mark

@mark.solution(test=21)
def pt1(data_file):
    def process_arr(arr, onums):
        nums = onums.copy()
        total = 0
        if not arr:
            return not nums or (not nums[0] and len(nums) == 1)
        if not nums:
            return all(i in ".?" for i in arr)
        if not nums[0]:
            if not arr[0] in ".?":
                return 0
            nums.pop(0)
            total+=process_arr(arr[1:], nums)
        else:
            if arr[0] == "#":
                num = nums[0]
                nums[0] -= num
                if len(arr) < num:
                    return 0
                if not all([i in "#?" for i in arr[:num]]):
                    return 0
                total+=process_arr(arr[num:], nums)
            elif arr[0] == ".":
                total+=process_arr(arr[1:], nums)
            else:
                for c in ".#":
                    total+=process_arr(c+arr[1:], nums)
        return total
    out = 0
    for data in [i.strip() for i in open(data_file).readlines()]:
        arr, nums = data.split()
        nums = [int(i) for i in nums.split(",")]
        out += process_arr(arr, nums)
    return out
        

@mark.solution(test=525152)
def pt2(data_file):
    memo = {}
    def process_arr(arr, onums):
        nums = onums.copy()
        if (arr, tuple(onums)) in memo:
            return memo[(arr, tuple(onums))]
        total = 0
        if not arr:
            return not nums or (not nums[0] and len(nums) == 1)
        if not nums:
            return all(i in ".?" for i in arr)
        if not nums[0]:
            if not arr[0] in ".?":
                return 0
            nums.pop(0)
            total+=process_arr(arr[1:], nums)
        else:
            if arr[0] == "#":
                num = nums[0]
                nums[0] -= num
                if len(arr) < num:
                    return 0
                if not all([i in "#?" for i in arr[:num]]):
                    return 0
                total+=process_arr(arr[num:], nums)
            elif arr[0] == ".":
                total+=process_arr(arr[1:], nums)
            else:
                for c in ".#":
                    total+=process_arr(c+arr[1:], nums)
        memo[(arr, tuple(onums))] = total
        return total
    out = 0
    for data in [i.strip() for i in open(data_file).readlines()]:
        arr, nums = data.split()
        nums = [int(i) for i in nums.split(",")]
        out += process_arr("?".join([arr]*5), nums*5)
    return out
    
@cache
def clean_process_arr(arr, nums):
    if not nums: 
        return "#" not in arr
    total = 0
    if len(arr) > nums[0] and arr[0] != ".":
        if "." not in arr[:nums[0]] and arr[nums[0]] != "#":
            total+=clean_process_arr(arr[nums[0]+1:], nums[1:])
    if arr and arr[0] != "#":
        total+=clean_process_arr(arr[1:], nums)
    return total

@mark.solution(test=21)
def clean_pt1(data_file):
    out = 0
    for data in [i.strip() for i in open(data_file).readlines()]:
        arr, nums = data.split()
        nums = tuple(int(i) for i in nums.split(","))
        out += clean_process_arr(arr+".", nums)
    return out
        
@mark.solution(test=525152)
def clean_pt2(data_file):
    out = 0
    for data in [i.strip() for i in open(data_file).readlines()]:
        arr, nums = data.split()
        nums = tuple(int(i) for i in nums.split(","))
        out += clean_process_arr("?".join([arr]*5)+".", nums*5)
    return out
    