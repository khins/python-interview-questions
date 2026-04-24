from questions.q008_contains_duplicate import contains_duplicate


def test_true():
    assert contains_duplicate([1,2,3,1]) is True


def test_false():
    assert contains_duplicate([1,2,3,4]) is False


def test_empty():
    assert contains_duplicate([]) is False


def test_many_duplicates():
    assert contains_duplicate([1,1,1,1]) is True