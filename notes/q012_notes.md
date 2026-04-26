# Q012 - Top K Frequent Elements

## Key Idea
🧠 Interview Explanation (how you’d say it)

“I use Python’s Counter to compute frequencies, then use most_common(k) to retrieve the top k elements, and extract just the numbers.”

Count frequency → extract top K
🧠 Big Picture First

This function answers:

“What are the k most frequent numbers in this list?”

So if:

nums = [1,1,1,2,2,3]
k = 2

We want:

[1,2]

---

## Steps

1. Build frequency map
2. Select top K elements

---

## Approaches

🧩 The Code
from collections import Counter

count = Counter(nums)
return [num for num, freq in count.most_common(k)]

🧱 Step 1: Count Frequencies,
   count = Counter(nums)

What is Counter?

Counter is a tool from the collections module that:

👉 counts how many times each element appears

### Sorting

* simple
* O(n log n)

### Heap

* efficient
* O(n log k)

### Bucket Sort

* optimal
* O(n)

---

## Pattern

Frequency counting + selection

---

## Takeaway

Use:

* dict → counting
* heap/buckets → ranking
