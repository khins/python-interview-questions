# q005_valid_parentheses.py

def is_valid(s: str) -> bool:
    """
    Check if parentheses are valid.

    Args:
        s (str): Input string of brackets

    Returns:
        bool: True if valid, False otherwise
    """
    # TODO: Implement
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack


if __name__ == "__main__":
    print(is_valid("()"))        # True
    print(is_valid("([)]"))      # False
    print(is_valid("{[]}"))      # True