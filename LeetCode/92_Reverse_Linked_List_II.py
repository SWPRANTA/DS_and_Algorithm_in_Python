from baseCode import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if not head or left == right:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move `prev` to the node just before the `left` position
    for _ in range(left - 1):
        prev = prev.next

    # Start reversing the sublist
    reverse_start = prev.next
    curr = reverse_start.next

    for _ in range(right - left):
        reverse_start.next = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = reverse_start.next
    
    return dummy.next

# Create a sample linked list
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

# Reverse the sublist between positions 2 and 4
res = reverseBetween(l, 2, 4)

printfrom(res)
