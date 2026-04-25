from questions.q010_valid_anagram import is_anagram


def test_true():
    assert is_anagram("anagram", "nagaram") is True

def test_true():
    assert is_anagram("jimmorrison", "mrmojorisin") is True


def test_false():
    assert is_anagram("rat", "car") is False


def test_empty():
    assert is_anagram("", "") is True


def test_different_lengths():
    assert is_anagram("a", "ab") is False


def test_case_sensitive():
    assert is_anagram("a", "A") is False