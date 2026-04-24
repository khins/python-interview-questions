# q008_contains_duplicate.py

def contains_duplicate(nums: list[int]) -> bool:
    """
    Check if any value appears at least twice.

    Args:
        nums (list[int]): List of integers

    Returns:
        bool: True if duplicates exist, False otherwise
    """
    # TODO: Implement
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

if __name__ == "__main__":
    print(contains_duplicate([1,2,3,1]))  # True
    print(contains_duplicate([1,2,3,4]))  # False

"""🧠 Why This Problem Matters

This is a pattern recognition problem:

👉 “Have I seen this before?”
→ Use a set

This same idea appears in:

Two Sum (you already did)
Sliding window problems
Frequency counting

🧠 Interview Explanation

“I use a set to track seen elements. As I iterate, if a number
already exists in the set, I return True. Otherwise, I add it.
This gives O(n) time complexity.”
"""