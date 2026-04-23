from questions.q003_fizzbuzz import fizzbuzz


def test_small():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_fifteen():
    result = fizzbuzz(15)
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"


def test_empty():
    assert fizzbuzz(0) == []


def test_one():
    assert fizzbuzz(1) == ["1"]