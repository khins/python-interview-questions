# q007_best_time_stock.py
"""
✅ Correct mindset:

👉 “What’s the cheapest price I’ve seen so far?”

Then:
👉 “If I sell today, what’s my profit?”
"""

def max_profit(prices: list[int]) -> int:
    """
    Calculate the maximum profit from a single buy/sell.

    Args:
        prices (list[int]): List of stock prices

    Returns:
        int: Maximum profit
    """
    # TODO: Implement
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


if __name__ == "__main__":
    print(max_profit([7,1,5,3,6,4]))  # 5
    print(max_profit([7,6,4,3,1]))    # 0

"""🧠 Interview Explanation
🧠 Interview Explanation

“I iterate once through the list, tracking the minimum price 
seen so far.
At each step, I calculate the profit if I sold at the current
price and update the maximum profit accordingly.
This gives O(n) time complexity.”
"""