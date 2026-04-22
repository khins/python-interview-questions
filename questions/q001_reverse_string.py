# q001_reverse_string.py

#  Pythonic slicing (most common)
def reverse_string(s: str) -> str:
    """
    Reverse a given string.

    Args:
        s (str): Input string

    Returns:
        str: Reversed string
    """
    # TODO: Implement this
    return s[::-1]

# Approach 1: Loop
def reverse_string_loop(s: str) -> str:
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result

# Approach 3: Using reversed()
def reverse_string_reversed(s: str) -> str:
    return "".join(reversed(s))

if __name__ == "__main__":
    print(reverse_string("hello"))   # expected: olleh
    print(reverse_string("Python"))  # expected: nohtyP
    print(reverse_string_loop("hello"))   # expected: olleh
    print(reverse_string_loop("Python"))  # expected: nohtyP
    print(reverse_string_reversed("hello"))   # expected: olleh
    print(reverse_string_reversed("Python"))  # expected: nohtyP