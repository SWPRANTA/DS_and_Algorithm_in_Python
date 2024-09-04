from baseCode import *
def rotateRight(head, k):
    if not head:
        return head
    length = 0
    temp = head
    tail = None
    while temp:
        tail = temp
        temp = temp.next
        length+=1
    if k==0:
        return head
    r = k%length
    temp = head
    for _ in range(length-r-1):
        temp = temp.next
    n = temp.next
    temp.next = None
    tail.next = head
    return n
l1 = LinkedList(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)


res = rotateRight(l1.head, 2)
printfrom(res)