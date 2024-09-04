from baseCode import Node, LinkedList, printfrom

def swapPairs(head):
    dummy = LinkedList(0)
    dummy.next = head
    temp = dummy
    while temp.next!=None and temp.next.next!=None:
        print("HH")
        fNode = temp.next
        sNode = temp.next.next

        fNode.next = sNode.next
        sNode.next = fNode
        temp.next = sNode
        

        temp = fNode
    
    return dummy.next


l1 = LinkedList(1)

l1.append(2)
l1.append(3)

res = swapPairs(l1.head)
printfrom(res)