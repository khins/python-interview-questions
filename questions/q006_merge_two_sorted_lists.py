# q006_merge_two_sorted_lists.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists and return the head.
    """
    # TODO: Implement
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

    # Append any remaining nodes from either list
    current.next = list1 or list2

    return dummy.next


# Helper functions (use these for testing/debugging)

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for v in values:
        current.next = ListNode(v)
        current = current.next

    return dummy.next


def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])

    merged = merge_two_lists(l1, l2)
    print(linked_list_to_list(merged))  # [1,1,2,3,4,4]