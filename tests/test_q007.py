from questions.q007_best_time_stock import max_profit


def test_basic():
    assert max_profit([7,1,5,3,6,4]) == 5


def test_no_profit():
    assert max_profit([7,6,4,3,1]) == 0


def test_single_day():
    assert max_profit([5]) == 0


def test_small():
    assert max_profit([2,4,1]) == 2