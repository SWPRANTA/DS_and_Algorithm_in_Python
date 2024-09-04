from baseCode import Node, LinkedList, printfrom


def reverseList(head):
    temp = head

    before = None

    while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    return before

def binToDecimal(head):
    rev = reverseList(head)
    cnt = 0
    result = 0
    while rev:
        result += (rev.val * pow(2, cnt))
        rev = rev.next
        cnt += 1
    
    return result


l1 = LinkedList(1)
l1.append(0)
l1.append(0)
l1.append(1)
l1.append(1)
l1.append(1)
l1.append(0)
l1.append(1)

res = binToDecimal(l1.head)
print(res)
