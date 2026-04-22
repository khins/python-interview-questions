# q002_palindrome.py

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.

    Args:
        s (str): Input string

    Returns:
        bool: True if palindrome, False otherwise
    """
    # TODO: Implement
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("madam"))    # True
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))    # False