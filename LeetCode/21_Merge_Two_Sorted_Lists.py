import time
st = time.process_time()
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
    
def mergeTwoLists(l1, l2):
    temp1 = l1.head
    temp2 = l2.head
    merged = LinkedList(0)
    while temp1!=None or temp2!=None:
        if temp1!=None and temp2!=None:
            if temp1.value < temp2.value:
                merged.append(temp1.value)
                temp1 = temp1.next
            elif temp1.value > temp2.value:
                merged.append(temp2.value)
                temp2 = temp2.next
            else:
                merged.append(temp1.value)
                merged.append(temp2.value)
                temp1 = temp1.next
                temp2 = temp2.next
        elif temp1==None and temp2!=None:
            print("here")
            merged.append(temp2.value)
            temp2 = temp2.next
        else:
            merged.append(temp1.value)
            temp1 = temp1.next
        merged.head = merged.head.next
    return merged

l1 = LinkedList(0)
l1.head = l1.head.next
l2 = LinkedList(2)

print("List 1:\n")
l1.print_list()
print("List 2:\n")
l2.print_list()

print("Merged List:")
merged = mergeTwoLists(l1, l2)
merged.print_list()

et = time.process_time()
res = et-st
print(f"Total process time: {res}")