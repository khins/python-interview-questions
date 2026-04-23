# Q005 - Valid Parentheses

## Key Idea

Use a stack (LIFO):

* Push opening brackets
* Pop when matching closing bracket appears

---

## Algorithm

1. Initialize empty stack
2. Loop through string:

   * If opening → push
   * If closing:

     * Check stack top
     * If mismatch → False
     * Else → pop
3. At end:

   * Stack must be empty

---

## Why Stack?

* Tracks most recent opening bracket
* Ensures correct nesting order

---

## Complexity

* Time: O(n)
* Space: O(n)

---

## Common Mistakes

* Not checking empty stack
* Mismatched pairs
* Forgetting final stack check

---

## Takeaway

Stacks are used for:

* Parsing expressions
* Syntax validation
* Depth tracking problems
