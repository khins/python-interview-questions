# q003_fizzbuzz.py

def fizzbuzz(n: int) -> list[str]:
    """
    Return a list of FizzBuzz values from 1 to n.

    Args:
        n (int): Upper limit

    Returns:
        list[str]: FizzBuzz sequence
    """
    # TODO: Implement
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

def fizzbuzz_advanced(n: int, rules: dict[int, str]) -> list[str]:
    """
    Example:
    rules = {3: "Fizz", 5: "Buzz"}
    """
    result = []
    for i in range(1, n + 1):
        entry = ""
        for divisor, word in rules.items():
            if i % divisor == 0:
                entry += word
        result.append(entry or str(i))
    return result


if __name__ == "__main__":
    print(fizzbuzz(15))
    print(fizzbuzz_advanced(15, {3: "Fizz", 5: "Buzz"}))