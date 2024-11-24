

def find_middle_node(head):
    slow = head
    fast = head
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    return slow
