def read_input(filename):
    rows = []
    with open(filename) as file:
        for line in file:
            item = line.rstrip()
            if item:
                row = [char == '#' for char in item]
                rows.append(row)
    return rows


def dimensions(trees):
    return (len(trees[0]), len(trees))


def has_tree(trees, x, y):
    try:
        return trees[y][x % width]
    except IndexError:
        return True


def move(x, y, x1, y1):
    return (x + x1, y + y1)


def count_trees(trees, x_slope, y_slope):
    x = y = 0
    count = 0
    while True:
        x, y = move(x, y, x_slope, y_slope)
        if y >= height:
            break
        if has_tree(trees, x, y):
            count += 1
    return count


tree_map = read_input('day3/input')
width, height = dimensions(tree_map)

total = 1
for coordinates in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    tree_count = count_trees(tree_map, *coordinates)
    total *= tree_count
    print(f'Path {coordinates} had {tree_count} trees')
print(f'Counts multiplied: {total}')
