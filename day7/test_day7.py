from day7 import day7


def test_color_parent():
    assert day7.color('light red bags') == 'light red'


def test_color_child_singular():
    assert day7.color('1 bright white bag') == 'bright white'


def test_color_child_plural():
    assert day7.color('2 muted yellow bags.') == 'muted yellow'


def test_learn_parents():
    extracted = day7.learn_parents('light red bags contain 1 bright white bag, 2 muted yellow bags.')
    assert extracted == {
        'bright white': {'light red'},
        'muted yellow': {'light red'}
    }


def test_learn_parents_no_children():
    extracted = day7.learn_parents('faded blue bags contain no other bags.')
    assert extracted == {}
