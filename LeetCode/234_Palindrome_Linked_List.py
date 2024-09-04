from baseCode import Node, LinkedList, printfrom

def isPalindrome(head):
    temp = head
    nodevals = []
    while temp:
        nodevals.append(temp.val)
        temp = temp.next
    
    return nodevals == nodevals[::-1]

l2 = LinkedList(1)
l2.append(2)
# l2.append(3)
l2.append(2)
l2.append(1)


res = isPalindrome(l2.head)
print(res)