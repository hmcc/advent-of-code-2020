def read_input(filename):
    rows = []
    with open(filename) as file:
        for line in file:
            item = line.rstrip()
            if item:
                row = [char for char in item]
                rows.append(row)
    return rows


def adjacent_seats(seat_map, column, row):
    adjacent = []
    for y in (row - 1, row, row + 1):
        if y < 0 or y >= len(seat_map):
            continue
        for x in (column - 1, column, column + 1):
            if x < 0 or x >= len(seat_map[0]):
                continue
            if x == column and y == row:
                continue
            adjacent.append(seat_map[y][x])
    return adjacent


def move_until_seat(seat_map, origin, direction):
    x, y = origin
    x1, y1 = direction
    while (x, y) == origin or (0 <= y < len(seat_map) and 0 <= x < len(seat_map[0]) and floor(seat_map[y][x])):
        x = x + x1
        y = y + y1
    return (x, y) if 0 <= y < len(seat_map) and 0 <= x < len(seat_map[0]) else None


def visible_seat_coordinates(seat_map, x, y):
    visible = []
    directions = (
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0)
    )
    for d in directions:
        visible_seat = move_until_seat(seat_map, (x, y), d)
        if visible_seat:
            visible.append(visible_seat)
    return visible


def visible_seats(seat_map, x, y):
    return [seat_map[y][x] for x, y in visible_seat_coordinates(seat_map, x, y)]


def empty(seat):
    return seat == 'L'


def floor(seat):
    return seat == '.'


def occupied(seat):
    return seat == '#'


def all_unoccupied(seat_list):
    return all([not occupied(seat) for seat in seat_list])


def five_or_more_occupied(seat_list):
    return [occupied(seat) for seat in seat_list].count(True) >= 5


def should_occupy(seat_map, x, y):
    return empty(seat_map[y][x]) and all_unoccupied(visible_seats(seat_map, x, y))


def should_vacate(seat_map, x, y):
    return occupied(seat_map[y][x]) and five_or_more_occupied(visible_seats(seat_map, x, y))


def should_flip(seat_map, x, y):
    return should_occupy(seat_map, x, y) or should_vacate(seat_map, x, y)


def flip(seat):
    if seat == '#':
        return 'L'
    if seat == 'L':
        return '#'
    return seat


def update(seat_map):
    new_seats = []
    for y, row in enumerate(seat_map):
        new_seats.append([])
        for x, _ in enumerate(row):
            if should_flip(seat_map, x, y):
                new_seats[y].append(flip(seat_map[y][x]))
            else:
                new_seats[y].append(seat_map[y][x])
    return new_seats


def pretty_print(seat_map):
    for row in seat_map:
        print(''.join(row))
    print()


def count_occupied(seat_map):
    return sum([row.count('#') for row in seat_map])


seats = read_input('day11/input')
pretty_print(seats)
prev_seats = [[None] * len(seats[0])] * len(seats)
while seats != prev_seats:
    prev_seats = seats
    seats = update(prev_seats)
    pretty_print(seats)

print(count_occupied(seats))
