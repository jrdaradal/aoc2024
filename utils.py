coords = tuple[int,int]
vector = tuple[coords,coords] # coords, direction
box    = tuple[coords,coords] # bounds

def getPath(day: int, full: bool) -> str:
    suffix = 'test' if full else 'sample'
    return 'data/%.2d_%s.txt' % (day, suffix)

def readLines(path: str, strip: bool = True) -> list[str]:
    f = open(path, 'r')
    if strip:
        lines = [x.strip() for x in f.readlines()]
    else:
        lines = [x for x in f.readlines()]
    f.close()
    return lines

def gridBounds(grid: list[str]) -> box:
    return ((0,0), (len(grid), len(grid[0])))

def isInsideBounds(c: coords, bounds: box) -> bool:
    (minRow,minCol),(maxRow,maxCol) = bounds 
    row,col = c 
    return minRow <= row and minCol <= col and row < maxRow and col < maxCol 
