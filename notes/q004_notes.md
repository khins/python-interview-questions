# Q004 - Two Sum (Walkthrough)

## 🧠 Problem Summary

Given:

* A list of integers `nums`
* A target integer `target`

Return:

* Indices of two numbers that add up to `target`

Constraints:

* Exactly one solution exists
* Cannot use the same element twice
* Must return indices (not values)

---

## 🔍 Core Idea

For each number:
complement = target - current_number

Instead of checking every pair, we:

* Store previously seen numbers
* Check if the complement already exists

---

## ❌ Approach 1: Brute Force

### Code Idea

* Use two loops
* Try every pair

### Walkthrough

Example:
nums = [2, 7, 11, 15], target = 9

Steps:

* Check (2,7) → 9 ✅ return [0,1]
* Stops early, but worst case checks all pairs

### Complexity

* Time: O(n²)
* Space: O(1)

---

## ✅ Approach 2: Hash Map (Optimal)

### Key Idea

Use a dictionary:
value → index

---

## 🔁 Step-by-Step Execution

### Input

nums = [2, 7, 11, 15]
target = 9

---

### Iteration 1

* i = 0
* num = 2
* complement = 9 - 2 = 7

Check:

* Is 7 in seen? ❌

Action:

* Store: {2: 0}

---

### Iteration 2

* i = 1
* num = 7
* complement = 9 - 7 = 2

Check:

* Is 2 in seen? ✅

Action:

* Return [0, 1]

---

## 📦 What "seen" Looks Like

At each step:

| Step | seen dictionary |
| ---- | --------------- |
| 1    | {2: 0}          |
| 2    | Found match     |

---

## ⚡ Why This Works

* Dictionary lookup is O(1)
* We avoid nested loops
* Each number processed once

---

## ⏱ Complexity

* Time: O(n)
* Space: O(n)

---

## ⚠️ Common Mistakes

* ❌ Adding element to dictionary before checking complement
* ❌ Returning values instead of indices
* ❌ Using same element twice
* ❌ Forgetting duplicates (e.g. [3,3])

---

## 🧠 Key Insight

Instead of asking:
"Can I find a pair?"

We ask:
"Have I already seen the number I need?"

---

## 🗣 Interview Explanation

“I start with a brute force approach using nested loops (O(n²)).
Then I optimize using a hash map to store previously seen values.
For each number, I compute the complement and check if it exists in constant time, reducing the complexity to O(n).”

---

## 🚀 Takeaways

* Hash maps = fast lookups
* Trade space for time
* This pattern appears in MANY problems

---

## 🔁 Pattern to Remember

1. Iterate through array
2. Compute complement
3. Check if complement exists
4. If yes → return result
5. If no → store current value
