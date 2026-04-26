from questions.q012_top_k_frequent import top_k_frequent, top_k_frequent_heap


def test_basic():
    assert set(top_k_frequent([1,1,1,2,2,3], 2)) == {1,2}


def test_single():
    assert top_k_frequent([1], 1) == [1]


def test_all_same():
    assert top_k_frequent([2,2,2], 1) == [2]

def test_k_equals_unique():
    assert set(top_k_frequent_heap([1,2,3], 3)) == {1,2,3}