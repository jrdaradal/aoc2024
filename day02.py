# 2024 Advent of Code Day 02 Solution
# John Roy Daradal 

# SolutionA: 490
# SolutionB: 536

from utils import * 

def input02(full: bool) -> list[list[int]]:
    return [[int(x) for x in line.split()] for line in readLines(getPath(2, full))]

def day02A():
    full = True
    count = 0 
    for numbers in input02(full):
        if isSafe(numbers):
            count += 1 
    print(count)

def day02B():
    full = True 
    count = 0 
    for numbers in input02(full):
        if isSafeV2(numbers):
            count += 1 
    print(count)

def isSafe(numbers: list[int]) -> bool:
    diffs = []
    for i in range(1,len(numbers)):
        diffs.append(numbers[i]-numbers[i-1])
    safeInc = all(1 <= d and d <= 3 for d in diffs)
    safeDec = all(-3 <=d  and d <= -1 for d in diffs)
    return safeInc or safeDec

def isSafeV2(numbers: list[int]) -> bool:
    remove = [None] + list(range(len(numbers)))
    for idx in remove:
        if idx is None:
            numbers2 = numbers[:]
        else:
            numbers2 = numbers[:idx] + numbers[idx+1:]
        if isSafe(numbers2):
            return True 
    return False

if __name__ == '__main__':
    day02A()
    day02B()