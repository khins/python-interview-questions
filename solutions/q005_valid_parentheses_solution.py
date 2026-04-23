# 🧠 Why This Works
# Stack keeps track of most recent opening bracket
# Ensures correct order + matching
# Mirrors real-world parsing logic
# ✅ Stack-Based Solution (Optimal)
# 🧠 Interview Explanation

# “I use a stack to track opening brackets.
# When encountering a closing bracket, I check if it matches
# the most recent opening bracket. If not, it's invalid.
# At the end, the stack must be empty.”

def is_valid(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in pairs:
            # closing bracket
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            # opening bracket
            stack.append(char)

    return len(stack) == 0

if __name__ == "__main__":
    print(is_valid("()"))        # True
    print(is_valid("([)]"))      # False
    print(is_valid("{[]}"))      # True