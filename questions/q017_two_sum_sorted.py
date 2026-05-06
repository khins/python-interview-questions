# q017_two_sum_sorted.py

def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """
    Return 1-based indices of two numbers that sum to target.

    Args:
        numbers (list[int]): sorted list of integers
        target (int): target sum

    Returns:
        list[int]: indices [i, j] (1-based)
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-based indices
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []  # Return empty list if no solution is found


if __name__ == "__main__":
    print(two_sum_sorted([2,7,11,15], 9))  # [1,2]