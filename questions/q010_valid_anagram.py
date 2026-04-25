# q010_valid_anagram.py

def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams.

    Args:
        s (str): first string
        t (str): second string

    Returns:
        bool: True if anagram, False otherwise
    """
    # TODO: implement
    if len(s) != len(t):
        return False

    # Count character frequencies
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrement counts using the second string
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]

    return len(char_count) == 0

from collections import Counter

def is_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False
    print(is_anagram_counter("anagram", "nagaram"))  # True

"""
🧠 Interview Explanation

“I count character frequencies in the first string, 
then decrement using the second string. If any count 
becomes negative or a character is missing, it’s not an anagram.”"""