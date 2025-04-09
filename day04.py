# 2024 Advent of Code Day 04 Solution
# John Roy Daradal 

# SolutionA: 2654
# SolutionB: 1990

from utils import *

def input04(full: bool) -> list[str]:
    return readLines(getPath(4, full))

def day04A():
    full = True 
    grid = input04(full)
    vectors = findStartingXM(grid)
    for letter in ('A','S'):
        vectors = findNextPositions(grid, vectors, letter)
    print(len(vectors))

def day04B():
    full = True 
    grid = input04(full)
    pts = findStartingA(grid)
    pts = findXMAS(grid, pts)
    print(len(pts))

def findStartingXM(grid: list[str]) -> list[vector]:
    pts: list[coords] = [(r,c) for r,line in enumerate(grid) for c,char in enumerate(line) if char == 'X']
    bounds = gridBounds(grid)
    vectors: list[vector] = []
    for center in pts:
        for v in surrounding(center, bounds):
            row,col = v[0]
            if grid[row][col] == 'M':
                vectors.append(v)
    return sorted(vectors)

def findNextPositions(grid: list[str], vectors: list[vector], letter: str) -> list[vector]:
    bounds = gridBounds(grid)
    vectors2 = []
    for v in vectors:
        c = getNext(v, bounds)
        if c is None: continue 
        row, col = c 
        if grid[row][col] == letter:
            vectors2.append((c,v[1]))
    return sorted(vectors2)

def getNext(v: vector, bounds: box) -> coords|None:
    (row,col),(drow,dcol) = v 
    c = ((row+drow),col+dcol)
    return c if isInsideBounds(c, bounds) else None

def surrounding(c: coords, bounds: box) -> list[vector]:
    row,col = c 
    near: list[vector] = [
        ((row-1,col-1), (-1,-1)),
        ((row-1,col),   (-1,0)),
        ((row-1,col+1), (-1,1)),
        ((row,col-1),   (0,-1)),
        ((row,col+1),   (0,1)),
        ((row+1,col-1), (1,-1)),
        ((row+1,col),   (1,0)),
        ((row+1,col+1), (1,1)),
    ]
    return list(filter(lambda v: isInsideBounds(v[0], bounds), near))

def findStartingA(grid: list[str]) -> list[coords]:
    innerBounds: box = [(1,1), (len(grid)-1, len(grid[0])-1)]
    pts: list[coords] = []
    for row,line in enumerate(grid):
        for col,item in enumerate(line):
            if item == 'A' and isInsideBounds((row,col), innerBounds):
                pts.append((row,col))
    return pts

def findXMAS(grid: list[str], centers: list[coords]) -> list[coords]:
    valid = []
    for c in centers:
        row,col = c 
        # left diag 
        tl = grid[row-1][col-1]
        br = grid[row+1][col+1]
        ldiag = tl + 'A' + br 
        # right diag 
        tr = grid[row-1][col+1]
        bl = grid[row+1][col-1]
        rdiag = tr + 'A' + bl 
        if isXMAS(ldiag, rdiag):
            valid.append(c)
    return valid 

def isXMAS(diag1: str, diag2: str):
    return all(d == 'MAS' or d == 'SAM' for d in (diag1,diag2))

if __name__ == '__main__':
    day04A()
    day04B()