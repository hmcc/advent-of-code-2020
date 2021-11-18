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


def empty(seat):
    return seat == 'L'


def occupied(seat):
    return seat == '#'


def all_unoccupied(seat_list):
    return all([not occupied(seat) for seat in seat_list])


def four_or_more_occupied(seat_list):
    return [occupied(seat) for seat in seat_list].count(True) >= 4


def should_occupy(seat_map, x, y):
    return empty(seat_map[y][x]) and all_unoccupied(adjacent_seats(seat_map, x, y))


def should_vacate(seat_map, x, y):
    return occupied(seat_map[y][x]) and four_or_more_occupied(adjacent_seats(seat_map, x, y))


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

print(count_occupied(seats))
