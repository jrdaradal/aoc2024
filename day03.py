# 2024 Advent of Code Day 03 Solution
# John Roy Daradal 

# SolutionA: 159833790
# SolutionB: 89349241

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

def day03B():
    full = True 
    text = input03(full)
    cmds = []
    for m in re.finditer(pattern, text):
        cmds.append((m.start(), m.group(0)))

    off = r"don't\(\)"
    on = r'do\(\)'
    regions = [(0,True)]
    for pat,flag in [(off,False), (on,True)]:
        for m in re.finditer(pat, text):
            regions.append((m.start(), flag))
    regions.sort(key=lambda x: x[0])

    ignore = []
    offStart = None 
    for start, flag in regions:
        if flag == False and offStart is None:
            offStart = start 
        elif flag == True and offStart is not None:
            ignore.append((offStart, start-1))
            offStart = None 
    if offStart is not None:
        ignore.append((offStart, len(text)-1))
    
    filterFn = lambda cmd: not any(x[0] <= cmd[0] and cmd[0] <= x[1] for x in ignore)
    total = 0 
    for _, cmd in filter(filterFn, cmds):
        total += execCommand(cmd)
    print(total)

def execCommand(cmd: str) -> int:
    cmd = cmd.strip('mul()')
    a,b = [int(x) for x in cmd.split(',')]
    return a*b

if __name__ == '__main__':
    day03A()
    day03B()