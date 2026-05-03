# q016_max_subarray.py
"""
✅ Key Insight (Kadane’s Algorithm)
At each position:
“Should I start fresh here, or extend previous subarray?”

🧠 Core Idea

For each number:

current_sum = max(num, current_sum + num)

👉 Either:

start new subarray at num
or extend previous one
🧠 Key Insight
Drop negative running sums—they hurt future totals

Negative sums are “dead weight”

Kadane automatically discards them.
"""

def max_subarray(nums: list[int]) -> int:
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6