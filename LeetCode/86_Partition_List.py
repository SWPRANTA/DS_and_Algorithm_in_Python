from baseCode import *
def partitionList(head, val):
    l = left = LinkedList(0)
    r = right = LinkedList(0)

    while head:
        if head.val < val:
            print(f"Adding {head.val} to the left")
            left.next = head
            left = left.next
        else:
            print(f"Adding {head.val} to the right")
            right.next = head
            right = right.next
        head = head.next
    left.next = r.next
    right.next = None
    return l.next

l = LinkedList(1)
l.append(4)
l.append(3)
l.append(2)
l.append(5)
l.append(2)

res = partitionList(l.head, 3)

res.print_list()