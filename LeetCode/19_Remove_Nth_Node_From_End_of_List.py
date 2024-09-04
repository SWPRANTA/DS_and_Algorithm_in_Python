from baseCode import *

def remove_nth_from_end(n, head):
    fast = slow = head
    temp = head
    for _ in range(n):
        fast = fast.next
    if fast is None:
        head = head.next
    else:
        while fast.next!=None:
            slow = slow.next
            fast = fast.next
        temp = slow.next
        slow.next = slow.next.next
        temp = None

    return head



l1 = LinkedList(5)
l1.append(1)
l1.append(6)
l1.append(7)
l1.append(10)
l1.append(9)
l1.append(3)

print("List 1:\n")
l1.print_list()
print("After Removing:")
removed = remove_nth_from_end(2, l1.head)

printfrom(removed)