from baseCode import *

def deleteDuplicates(head):
    current = head
    prev = Node(0)
    prev.next = head
    head = prev
    while current and current.next:
        if current.val == current.next.val:
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            current = current.next
            prev.next = current
        else:
            current = current.next
            prev = prev.next
    return head.next

l = LinkedList(1)
l.append(2)
l.append(3)
l.append(3)
l.append(4)
l.append(4)
l.append(5)

res = deleteDuplicates(l.head)
printfrom(res)