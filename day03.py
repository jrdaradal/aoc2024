# 2024 Advent of Code Day 03 Solution
# John Roy Daradal 

# SolutionA: 159833790

import re
from utils import * 

pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'

def input03(full: bool) -> str:
    return ''.join(readLines(getPath(3, full)))

def day03A():
    full = True 
    total = 0 
    for cmd in re.findall(pattern, input03(full)):
        total += execCommand(cmd)
    print(total)

def execCommand(cmd: str) -> int:
    cmd = cmd.strip('mul()')
    a,b = [int(x) for x in cmd.split(',')]
    return a*b

if __name__ == '__main__':
    day03A()