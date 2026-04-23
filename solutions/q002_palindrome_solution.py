import re

# Approach 1: Reverse comparison
def is_palindrome_simple(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]


# Approach 2: Two-pointer (interview favorite)
def is_palindrome_two_pointer(s: str) -> bool:
    s = re.sub(r'[^a-z0-9]', '', s.lower())

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

if __name__ == "__main__":
    print(is_palindrome_simple("A man a plan a canal Panama"))  # True
    print(is_palindrome_two_pointer("A  man a plan a canal Panama"))  # True