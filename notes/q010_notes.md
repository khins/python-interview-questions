# Q010 - Valid Anagram

## Key Idea

Compare character frequencies using a hash map.

---

## Algorithm

1. If lengths differ → return False
2. Count characters in s
3. Decrement using t
4. If any count < 0 → False
5. Otherwise → True

---

## Complexity

* Time: O(n)
* Space: O(1) or O(n)

---

## Alternative

Use Counter:
Counter(s) == Counter(t)

---

## Pattern

Frequency counting using hash maps

---

## Takeaway

Use hash maps when:

* counting occurrences
* comparing frequencies
