# q012_top_k_frequent.py

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Return the k most frequent elements.

    Args:
        nums (list[int]): list of integers
        k (int): number of top elements

    Returns:
        list[int]: k most frequent elements
    """
    # TODO: implement
    from collections import Counter
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]

def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        buckets[count].append(num)

    result = []

    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result


if __name__ == "__main__":
    print(top_k_frequent([1,1,1,2,2,3], 2))  # [1,2]
    print(top_k_frequent_heap([1,1,1,2,2,3], 2))  # [1,2]