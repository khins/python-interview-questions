# Question 4: Two Sum
# Given an array of integers `nums` and an integer `target`, return indices of the  
# two numbers such that they add up to `target`.
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value → index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
    return []  # Return empty if no solution found

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))  # [1, 2]
