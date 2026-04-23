from questions.q005_valid_parentheses import is_valid


def test_valid_simple():
    assert is_valid("()") is True


def test_valid_multiple():
    assert is_valid("()[]{}") is True


def test_invalid_mismatch():
    assert is_valid("(]") is False


def test_invalid_order():
    assert is_valid("([)]") is False


def test_nested_valid():
    assert is_valid("{[]}") is True


def test_empty():
    assert is_valid("") is True