class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, val):
        new_node = Node(val)
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
            print(temp.val)
            temp = temp.next
    

def printfrom(head):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next
