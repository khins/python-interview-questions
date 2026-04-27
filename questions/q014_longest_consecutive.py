# q014_longest_consecutive.py

def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    num_set = set(nums)
    longest = 1

    for num in num_set:
        if num - 1 not in num_set:  # Start of a sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest

def longest_consecutive_in_sequence(nums: list[int]) -> int:
    # return as [1,2,3,4] instead of 4
    if not nums:
        return []   
    
    num_set = set(nums)
    longest = []

    for num in num_set:
        if num - 1 not in num_set:  # Start of a sequence
            current_num = num
            current_streak = [current_num]

            while current_num + 1 in num_set:
                current_num += 1
                current_streak.append(current_num)

            if len(current_streak) > len(longest):
                longest = current_streak
    
    return longest

if __name__ == "__main__":
    print(longest_consecutive([100,4,200,1,3,2]))  # 4
    print(longest_consecutive_in_sequence([100,4,200,1,3,2]))  # [1,2,3,4]