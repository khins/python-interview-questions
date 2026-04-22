from questions.q002_palindrome import is_palindrome


def test_basic_true():
    assert is_palindrome("madam") is True


def test_basic_false():
    assert is_palindrome("hello") is False


def test_empty():
    assert is_palindrome("") is True


def test_single_char():
    assert is_palindrome("a") is True


def test_case_insensitive():
    assert is_palindrome("Racecar") is True


def test_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True