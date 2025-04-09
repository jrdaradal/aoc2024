# 2024 Advent of Code Day 02 Solution
# John Roy Daradal 

# SolutionA: 490

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

def isSafe(line):
    diffs = []
    for i in range(1,len(line)):
        diffs.append(line[i]-line[i-1])
    safeInc = all(1 <= d and d <= 3 for d in diffs)
    safeDec = all(-3 <=d  and d <= -1 for d in diffs)
    return safeInc or safeDec

if __name__ == '__main__':
    day02A()