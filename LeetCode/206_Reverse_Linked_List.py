from baseCode import LinkedList, Node, printfrom


def reverseList(head):
    temp = head

    before = None

    while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    return before

l2 = LinkedList(7)
l2.append(6)
l2.append(1)
l2.append(5)
l2.append(8)
l2.append(5)

l2.print_list()

print("Reversed:")
res = reverseList(l2.head)

printfrom(res)