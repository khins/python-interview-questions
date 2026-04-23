"""🔍 Step-by-Step (Mental Model)
l1: 1 → 2 → 4
l2: 1 → 3 → 4

Compare heads:

1 vs 1 → pick one
move pointer
repeat

You are stitching nodes together, not creating new ones.

🧠 What This Teaches
Pointer manipulation
Linked list traversal
Dummy node pattern (VERY important)
Recursion vs iteration tradeoffs
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # Attach remaining nodes
    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next

# 🔁 Approach 2: Recursive (Advanced)
def merge_two_lists_recursive(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2
    
"""🧠 Interview Explanation

“I use a dummy node to simplify edge cases. 
I iterate through both lists, always attaching the
smaller node and advancing pointers. Once one list is 
exhausted, I attach the remainder.”"""