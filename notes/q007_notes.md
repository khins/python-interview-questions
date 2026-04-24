# Q007 - Best Time to Buy/Sell Stock

## Key Idea

Track minimum price so far and compute profit at each step.

---

## Algorithm

1. Initialize:

   * min_price = infinity
   * max_profit = 0

2. Loop through prices:

   * Update min_price
   * Calculate profit = current_price - min_price
   * Update max_profit

---

## Why This Works

* Always buying at the lowest possible price before selling
* Single pass (greedy approach)

---

## Complexity

* Time: O(n)
* Space: O(1)

---

## Common Mistakes

* Trying brute force (O(n²))
* Updating profit before min_price
* Not handling decreasing prices

---

## Takeaway

Greedy = make best decision at each step using past info
