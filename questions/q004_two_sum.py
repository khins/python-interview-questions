# q004_two_sum.py

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find indices of two numbers that add up to target.

    Args:
        nums (list[int]): List of integers
        target (int): Target sum

    Returns:
        list[int]: Indices of the two numbers
    """
    # TODO: Implement
    num_to_index = {}   
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []  # Return empty if no solution found


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]