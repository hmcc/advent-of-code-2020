def readInput(filename):
    map = []
    with open(filename) as file:
        for line in file:
            item = line.rstrip()
            if(item):
                row = [char=='#' for char in item]
                map.append(row)
    return map

def dimensions(map):
    return (len(map[0]), len(map))

def hasTree(map, x, y):
    try:
        return map[y][x % width]
    except IndexError:
        return True

def move(x, y, x1, y1):
    return (x + x1, y + y1)

def countTrees(xSlope, ySlope):
    x = y = 0
    treeCount = 0
    while True:
        x, y = move(x, y, xSlope, ySlope)
        if y >= height:
            break
        if(hasTree(map, x, y)):
            treeCount += 1
    return treeCount


map = readInput('input')
width, height = dimensions(map)

total = 1
for coordinates in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    treeCount = countTrees(*coordinates)
    total *= treeCount
    print(f'Path {coordinates} had {treeCount} trees')
print(f'Counts multiplied: {total}')