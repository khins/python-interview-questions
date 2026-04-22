# test_q001.py

from questions.q001_reverse_string import reverse_string


def test_basic():
    assert reverse_string("hello") == "olleh"


def test_empty():
    assert reverse_string("") == ""


def test_single_char():
    assert reverse_string("a") == "a"


def test_palindrome():
    assert reverse_string("madam") == "madam"


def test_intentional_failure():
    assert reverse_string("hello") == "hello"
