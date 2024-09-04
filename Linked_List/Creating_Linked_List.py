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
    
    def pop(self):
        if self.length == 0:
            print("Nothing to pop. The list is empty...")
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            pre = self.head
            while temp.next != None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp
        
    def prepend(self, value):
        if self.length == 0:
            self.append(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0 or self.length == 1:
            self.pop()
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        return temp
    
    def get(self, index):
        if index<0 or index>self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set_value(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, value, index):
        if index<0 or index>self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
    
    def remove(self, index):
        if index<0 or index>=self.length:
            return None
        elif index==0:
            return self.pop_first()
        elif index==self.length-1:
            return self.pop()
        else:
            pre = self.get(index-1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp
    
    def reverse(self):
        if self.length == 0 or self.length == 1:
            print("Nothing to reverse...")
        else:
            temp = self.head
            self.head = self.tail
            self.tail = temp
            before = None
            for _ in range(self.length):
                after = temp.next
                temp.next = before
                before = temp
                temp = after

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    ##LeetCode Problem1: Find the middle node without using the length of the Linked List
    def find_middle_node(self):
        temp1 = self.head
        temp2 = self.head

        while temp2 is not None and temp2.next is not None :
            temp1 = temp1.next
            temp2 = temp2.next.next
        
        return temp1
    
    ##LeetCode Porblem2: Write a method called has_loop that is part of the linked list class
    def has_loop(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
    ##LeetCode Porblem3: Removing the duplicate values from a singly linked list of integer values preserving the relative order
    def remove_duplicates(self):
        theset = set()
        temp = self.head
        pre = self.head

        while temp.next != None:
            if temp.value not in theset:
                theset.add(temp.value)
                pre = temp
                temp = temp.next
            else:
                temp = temp.next
                pre.next = temp
                self.length -= 1
        if temp.value in theset:
            pre.next = None
            self.length -= 1
        else:
            pre = temp
        self.tail = pre
        self.tail.next = None
    ##LeetCode Problem4: Find Kth Node From End
    def find_kth_from_end(self, k):
        slow = self.head
        fast = self.head
        
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow
    
    ##LeetCode Problem5: Reverse Between
    def reverse_between(self, m, n):
        mthprev = self.get(m-1)
        mth = self.get(m)
        nth = self.get(n)
        print(f"prev: {mthprev.value}... mth: {mth.value}... nth: {nth.value}")
        temp = mth
        after = mth.next
        before = mthprev
        while after.value != nth.value:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_list = LinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)



print("Original List:\n")
my_list.print_list()

# print(f"Middle node: {my_list.find_middle_node().value}")

# print(f"Middle Node: {my_list.find_middle_node().value}")
# print(f"Has Loop: {my_list.has_loop()}")
# my_list.remove_duplicates()
# print(f"After Removing Duplicates:")
# my_list.print_list()
# k = int(input("Finding kth node from end:"))
# k = 2
# node = my_list.find_kth_from_end(k)
# if node is None:
#     print(node)
# else:
#     print(node.value)

print("After reversing between m and n: ")
my_list.reverse_between(2, 4)
my_list.print_list()
# print(my_list.head.next.next.next.value)
# print(my_list.head, " " ,my_list.tail," ", my_list.head.value)