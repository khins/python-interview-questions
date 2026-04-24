# q009_product_except_self.py
# answer[i] = (product of everything LEFT of i) × (product of everything RIGHT of i)

def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    # Calculate the product of all elements to the left of each index
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    # Calculate the product of all elements to the right of each index
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer


if __name__ == "__main__":
    print(product_except_self([1,2,3,4]))        # [24,12,8,6]
    print(product_except_self([-1,1,0,-3,3]))    # [0,0,9,0,0]
