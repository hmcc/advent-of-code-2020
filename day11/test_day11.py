import pytest

from day11 import day11


seats = day11.read_input('day11/input_sample')
seats_flipped = day11.update(seats)


@pytest.mark.parametrize('origin_coordinates,adjacent_coordinates', [
    ((0, 0), ((1, 0), (0, 1), (1, 1))),                  # top left corner
    ((9, 9), ((8, 8), (9, 8), (8, 9))),                  # bottom right corner
    ((2, 0), ((1, 0), (3, 0), (1, 1), (2, 1), (3, 1))),  # top edge
    ((9, 1), ((8, 0), (9, 0), (8, 1), (8, 2), (9, 2))),  # right edge
    ((4, 4), (                                           # middle
        (3, 3), (4, 3), (5, 3),
        (3, 4), (5, 4),
        (3, 5), (4, 5), (5, 5)
    ))
])
def test_adjacent_seats(origin_coordinates, adjacent_coordinates):
    column, row = origin_coordinates
    expected_output = [seats[y][x] for x, y in adjacent_coordinates]
    assert day11.adjacent_seats(seats, column, row) == expected_output


@pytest.mark.parametrize('seat_list,expected_result', [
    ([], True),
    (['.'], True),
    (['L', 'L'], True),
    (['.', 'L', 'L'], True),
    (['#'], False),
    (['#', '#'], False),
    (['#', '.'], False),
])
def test_all_unoccupied(seat_list, expected_result):
    assert day11.all_unoccupied(seat_list) == expected_result


@pytest.mark.parametrize('seat_list,expected_result', [
    (['#'], False),
    (['#', '#'], False),
    (['#', '#', '#', '#', '#'], True),
    (['.', '#', '#', '#', '#', '#'], True),
    (['#', '#', '#', '#', '.', '#', 'L'], True),
])
def test_five_or_more_occupied(seat_list, expected_result):
    assert day11.five_or_more_occupied(seat_list) == expected_result


@pytest.mark.parametrize('coordinates,expected_result', [
    ((0, 0), True),
    ((1, 0), False),  # floor
    ((2, 0), True),
    ((1, 1), True),
    ((9, 9), True),
])
def test_should_occupy(coordinates, expected_result):
    column, row = coordinates
    assert day11.should_occupy(seats, column, row) is expected_result


@pytest.mark.parametrize('coordinates,expected_result', [
    ((0, 0), False),  # corner, not enough surrounding occupied seats
    ((1, 0), False),  # floor
    ((2, 0), True),
    ((1, 1), True),
    ((9, 9), False),  # corner
])
def test_should_vacate(coordinates, expected_result):
    column, row = coordinates
    assert day11.should_vacate(seats_flipped, column, row) is expected_result


def test_flip():
    row = ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L']
    new_row = ['#', '.', '#', '#', '.', '#', '#', '.', '#', '#']
    assert [day11.flip(seat) for seat in row] == new_row
    assert [day11.flip(seat) for seat in new_row] == row


def test_visible_seat_coordinates_all():
    """
    From the first example in Part Two
    .......#.
    ...#.....
    .#.......
    .........
    ..#L....#
    ....#....
    .........
    #........
    ...#.....
    """

    seat_map = [
        ['.', '.', '.', '.', '.', '.', '.', '#', '.'],
        ['.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ['.', '#', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '#', 'L', '.', '.', '.', '.', '#'],
        ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '#', '.', '.', '.', '.', '.']
    ]
    x = 3
    y = 4
    assert seat_map[y][x] == 'L'

    expected = [
        (1, 2), (3, 1), (7, 0), (8, 4), (4, 5), (3, 8), (0, 7), (2, 4)
    ]
    assert day11.visible_seat_coordinates(seat_map, x, y) == expected


def test_visible_seat_coordinates_some():
    """
    From the second example in Part Two
    .............
    .L.L.#.#.#.#.
    .............
    """

    seat_map = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', 'L', '.', 'L', '.', '#', '.', '#', '.', '#', '.', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]
    x = 1
    y = 1
    assert seat_map[y][x] == 'L'

    expected = [
        (3, 1)
    ]
    assert day11.visible_seat_coordinates(seat_map, x, y) == expected


def test_visible_seat_coordinates_none():
    """
    From the final example in Part Two
    .##.##.
    #.#.#.#
    ##...##
    ...L...
    ##...##
    #.#.#.#
    .##.##.
    """

    seat_map = [
        ['.', '#', '#', '.', '#', '#', '.'],
        ['#', '.', '#', '.', '#', '.', '#'],
        ['#', '#', '.', '.', '.', '#', '#'],
        ['.', '.', '.', 'L', '.', '.', '.'],
        ['#', '#', '.', '.', '.', '#', '#'],
        ['#', '.', '#', '.', '#', '.', '#'],
        ['.', '#', '#', '.', '#', '#', '.'],
    ]
    x = 3
    y = 3
    assert seat_map[y][x] == 'L'

    assert len(day11.visible_seat_coordinates(seat_map, x, y)) == 0
