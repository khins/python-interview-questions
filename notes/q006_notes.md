# Q006 - Merge Two Sorted Lists

## Key Idea

Use two pointers to traverse both lists and merge them in sorted order.

---

## Algorithm

1. Create dummy node
2. Use current pointer
3. Compare list1.val and list2.val:

   * Attach smaller node
   * Move that list forward
4. Move current forward
5. Attach remaining nodes

---

## Why Dummy Node?

* Simplifies head handling
* Avoids edge cases

---

## Complexity

* Time: O(n + m)
* Space: O(1)

---

## Common Mistakes

* Losing node references
* Not attaching remainder
* Forgetting to move pointers

---

## Takeaway

Linked lists require:

* Pointer thinking (not indexing)
* Careful reference handling
