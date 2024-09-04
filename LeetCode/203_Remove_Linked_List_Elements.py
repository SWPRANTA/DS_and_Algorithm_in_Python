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
def printfrom(head):
    temp = head
    while temp is not None:
        print(temp.value)
        temp = temp.next
def removeElements(head, val):
    dummy = Node(0)
    dummy.next = head
    temp = head
    pre = dummy
    while temp!=None:
        if temp.value == val:
            pre.next = temp.next
            temp = temp.next
        else:
            pre = pre.next
            temp = temp.next
    dummy = dummy.next
    return dummy
l2 = LinkedList(5)
l2.append(6)
l2.append(1)
l2.append(5)
l2.append(8)
l2.append(5)
res = removeElements(l2.head, 5)
printfrom(res)
