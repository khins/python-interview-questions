# Approach 1: Standard
def fizzbuzz(n: int) -> list[str]:
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


# Approach 2: Cleaner concatenation
def fizzbuzz_clean(n: int) -> list[str]:
    result = []

    for i in range(1, n + 1):
        output = ""

        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"

        result.append(output if output else str(i))

    return result


# 🔥 Approach 3: Dynamic rules (interview gold)
def fizzbuzz_advanced(n: int, rules: dict[int, str]) -> list[str]:
    result = []

    for i in range(1, n + 1):
        output = ""

        for divisor, word in rules.items():
            if i % divisor == 0:
                output += word

        result.append(output if output else str(i))

    return result