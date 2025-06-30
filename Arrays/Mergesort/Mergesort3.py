class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sortList(head)
    right = sortList(mid)

    return merge(left, right)

def merge(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next

# --- 🔁 UNIVERSAL TEST FUNCTION ---
def test_sort_linked_list(values):
    # Convert Python list to linked list
    head = None
    for val in reversed(values):
        head = ListNode(val, head)

    # Sort the list
    sorted_head = sortList(head)

    # Convert back to Python list for output
    result = []
    while sorted_head:
        result.append(sorted_head.val)
        sorted_head = sorted_head.next

    print("Input: ", values)
    print("Sorted:", result)
    print('-' * 40)



# --- ✅ TESTS ---
test_sort_linked_list([4, 2, 1, 3])
test_sort_linked_list([7, 3, 9, 1, 6, 2, 10, 5, 8, 4, 12, 11, 0])
test_sort_linked_list([5])
test_sort_linked_list([])
test_sort_linked_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
