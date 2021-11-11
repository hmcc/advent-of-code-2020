from day8 import day8


def test_parse_line_nop():
    assert day8.parse_line('nop +0') == ['nop', 0]


def test_parse_line_acc():
    assert day8.parse_line('acc +1') == ['acc', 1]


def test_parse_line_jmp():
    assert day8.parse_line('jmp -3') == ['jmp', -3]
