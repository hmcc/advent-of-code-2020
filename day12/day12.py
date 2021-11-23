def read_and_process(filename):
    north = east = 0
    facing = 'E'
    with open(filename) as file:
        for line in file:
            item = line.rstrip()
            direction, amount = item[:1], int(item[1:])
            north, east, facing = update(north, east, facing, direction, amount)
    return north, east


def update(north, east, facing, direction, amount):
    if direction == 'N':
        north += amount
    elif direction == 'E':
        east += amount
    elif direction == 'S':
        north -= amount
    elif direction == 'W':
        east -= amount
    elif direction == 'F':
        return update(north, east, facing, facing, amount)
    elif direction == 'L':
        facing = rdegrees_to_direction(360 - amount, facing)
    elif direction == 'R':
        facing = rdegrees_to_direction(amount, facing)

    return north, east, facing


def rdegrees_to_direction(rdegrees, prev):
    lr_order = ('N', 'E', 'S', 'W')
    current_pos = lr_order.index(prev)
    steps = int(rdegrees / 90)
    new_pos = (current_pos + steps) % 4
    return lr_order[new_pos]

north, east = read_and_process('day12/input')
distance = abs(north) + abs(east)
print(distance)
