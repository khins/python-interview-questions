# Q008 - Contains Duplicate

## Key Idea

Use a set to track seen values.

---

## Approaches

### 1. Set Length

* Compare len(nums) vs len(set(nums))
* Simple and clean

### 2. Manual Set

* Iterate and check membership
* Allows early exit

---

## Complexity

* Time: O(n)
* Space: O(n)

---

## Pattern

"Have I seen this before?" → Use a set

---

## Common Mistakes

* Using nested loops (O(n²))
* Sorting unnecessarily
* Not exiting early

---

## Takeaway

Sets provide O(1) lookup → critical for performance
