class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


def addTwoNumbers(l1, l2):
    carry = 0
    sumlist = LinkedList(0)

    while l1!=None or l2!=None:
        if l1!=None and l2!=None:
            s = l1.value + l2.value + carry
        elif l1 == None and l2!=None:
            s = 0 + l2.value + carry
        elif l1 != None and l2==None:
            s = l1.value + 0 + carry
        else:
            s = carry
        print(s)
        carry = int(s/10)
        s = int(s%10)
        sumlist.append(s)
        print(f"s: {s}... carry: {carry}")
        if l1!=None:
            l1 = l1.next
        if l2!=None:
            l2 = l2.next
    if carry!=0:
        sumlist.append(carry)
    sumlist.head = sumlist.head.next
    return sumlist

l1 = LinkedList(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l2 = LinkedList(9)
l2.append(9)
l2.append(9)
l2.append(9)
print("List 1:\n")
l1.print_list()
print("List 2:\n")
l2.print_list()

sumlist = addTwoNumbers(l1.head, l2.head)
print("\n\n")
sumlist.print_list()
print(sumlist.head)
print(sumlist)

