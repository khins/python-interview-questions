# q015_valid_parentheses.py

def is_valid(s: str) -> bool:
    # TODO
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)


if __name__ == "__main__":
    print(is_valid("()"))        # True
    print(is_valid("([)]"))      # False