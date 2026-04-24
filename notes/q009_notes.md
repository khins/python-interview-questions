# Q009 - Product of Array Except Self (Insights)

## Key Idea

Each element = product of:

* everything to the left
* everything to the right

---

## Approach

1. First pass:

   * store prefix (left) products

2. Second pass:

   * multiply suffix (right) products

---

## Why It Works

* Avoids division
* Reuses output array
* Efficient two-pass solution

---

## Complexity

* Time: O(n)
* Space: O(1) (excluding output)

---

## Key Pattern

"Prefix + Suffix computation"

---

## Interview Insight

Explain clearly:

* first pass builds prefix
* second pass applies suffix

---

## Edge Case

Handles zeros naturally without special logic
