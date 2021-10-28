from day5 import day5


def test_decode_examples():
    assert day5.decode('BFFFBBFRRR') == (70, 7)
    assert day5.decode('FFFBBBFRRR') == (14, 7)
    assert day5.decode('BBFFBBFRLL') == (102, 4)


def test_seat_id_examples():
    assert day5.seat_id('BFFFBBFRRR') == 567
    assert day5.seat_id('FFFBBBFRRR') == 119
    assert day5.seat_id('BBFFBBFRLL') == 820
