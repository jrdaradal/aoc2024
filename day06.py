# 2024 Advent of Code Day 06 Solution
# John Roy Daradal 

# SolutionA: 4988

from utils import * 

class Config:
    def __init__(self):
        self.rows = 0 
        self.cols = 0 
        self.blocked: dict[coords,bool] = {}
        self.pos: coords = (0,0)
        self.dir: coords = (0,0)

    @property 
    def bounds(self) -> box:
        return ((0,0),(self.rows, self.cols))

def input06(full: bool) -> Config:
    cfg = Config()
    lines = readLines(getPath(6, full))
    cfg.rows, cfg.cols = len(lines), len(lines[0])
    for row,line in enumerate(lines):
        for col,char in enumerate(line):
            if char == '#':
                cfg.blocked[(row,col)] = True 
            elif char == '^':
                cfg.pos = (row,col)
                cfg.dir = (-1,0)
    return cfg

def day06A():
    full = True
    count = countStepsExit(input06(full))
    print(count)

def countStepsExit(cfg: Config) -> int:
    pos, dir = cfg.pos, cfg.dir 
    bounds = cfg.bounds
    visited: set[coords] = set()
    visited.add(pos)
    while True:
        (row,col),(dy,dx) = pos,dir 
        row2,col2 = row+dy, col+dx 
        nxt = (row2,col2)

        if not isInsideBounds(nxt, bounds):
            break 
        elif cfg.blocked.get(nxt, False):
            dir = turnRight(dir)
        else:
            pos = nxt 
            visited.add(pos)
    return len(visited)

def turnRight(dir: coords) -> coords:
    if dir == (-1,0):   # N to E
        return (0,1)
    elif dir == (0,1):  # E to S 
        return (1,0)
    elif dir == (1,0):  # S to W 
        return (0,-1)
    elif dir == (0,-1): # W to N 
        return (-1,0)

if __name__ == '__main__':
    day06A()