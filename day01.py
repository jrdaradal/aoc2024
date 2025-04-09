# 2024 Advent of Code Day 01 Solution
# John Roy Daradal 

# SolutionA: 1834060

from utils import * 

def input01(full: bool) -> tuple[list[int],list[int]]:
    col1, col2 = [], []
    for line in readLines(getPath(1, full)):
        a,b = line.split()
        col1.append(int(a))
        col2.append(int(b))
    return col1, col2 

def day01A():
    full = True
    col1, col2 = input01(full)
    col1.sort() 
    col2.sort() 
    total = 0
    for a,b in zip(col1, col2):
        total += abs(a-b)
    print(total)

if __name__ == '__main__':
    day01A()