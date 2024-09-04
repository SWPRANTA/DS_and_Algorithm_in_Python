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
def getIntersectionNode(hA, hB):
    nodes = set()
    while hA:
        nodes.add(hA)
        hA = hA.next
    while hB:
        if hB in nodes:
            return hB
        else:
            hB = hB.next
    return hB
l1 = LinkedList(4)
l1.append(1)

l2 = LinkedList(5)
l2.append(6)
l2.append(1)
l2.append(8)

l1.tail.next = l2.tail

l2.append(4)
l2.append(5)

# print("l1")
# l1.print_list()
# print("l2")
# l2.print_list()

res = getIntersectionNode(l1.head, l2.head)

print(res.value)