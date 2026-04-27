from questions.q013_encode_decode_strings import encode, decode


def test_basic():
    data = ["hello", "world"]
    assert decode(encode(data)) == data


def test_empty_string():
    data = ["", "abc"]
    assert decode(encode(data)) == data


def test_special_chars():
    data = ["#", "##", "a#b"]
    assert decode(encode(data)) == data


def test_empty_list():
    data = []
    assert decode(encode(data)) == data