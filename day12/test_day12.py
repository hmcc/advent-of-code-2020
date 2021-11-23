import pytest

from day12 import day12


@pytest.mark.parametrize('direction,amount,position', [
    ('N', 3, (0, 3)),
    ('E', 5, (5, 0)),
    ('S', 2, (0, -2)),
    ('W', 1, (-1, 0)),
])
def test_update_nsew(direction, amount, position):
    initial_facing = 'E'
    north, east, facing = day12.update(0, 0, initial_facing, direction, amount)
    assert (east, north) == position
    assert facing == initial_facing


@pytest.mark.parametrize('initial_facing,amount,position', [
    ('N', 3, (0, 3)),
    ('E', 5, (5, 0)),
    ('S', 2, (0, -2)),
    ('W', 1, (-1, 0)),
])
def test_update_forward(initial_facing, amount, position):
    direction = 'F'
    north, east, facing = day12.update(0, 0, initial_facing, direction, amount)
    assert (east, north) == position
    assert facing == initial_facing


@pytest.mark.parametrize('direction,degrees,expected_facing', [
    ('R', 90, 'E'),
    ('L', 90, 'W'),
    ('R', 180, 'S'),
    ('L', 180, 'S'),
    ('R', 270, 'W'),
    ('L', 360, 'N'),
    ('R', 450, 'E'),
])
def test_update_turn(direction,degrees,expected_facing):
    initial_facing = 'N'
    north, east, facing = day12.update(0, 0, initial_facing, direction, degrees)
    assert (east, north) == (0, 0)
    assert facing == expected_facing
