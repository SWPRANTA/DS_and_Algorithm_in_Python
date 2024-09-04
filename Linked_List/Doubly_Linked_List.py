class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, val):
        node = Node(val)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def prepend(self, val):
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        lastP = self.tail
        if (self.head == self.tail) and self.head:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            lastP.prev = None
            self.tail.next = None
        self.length -= 1
        return lastP

    def popFirst(self):
        if self.head is None:
            return None
        temp = self.head
        if ((self.head == self.tail) and self.head):
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in (self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_val(self, index, val):
        temp = self.get(index)
        if temp:
            temp.val = val
            return True
        return False

    def insert_val(self, index, val):
        newNode = Node(val)
        if index < 0 or index > self.length:
            return False
        else:
            if index == 0:
                return self.prepend(val)
            if index == self.length:
                return self.append(val)
            temp = self.get(index)
            bef = temp.prev
            bef.next = newNode
            newNode.prev = bef
            newNode.next = temp
            temp.prev = newNode
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

    def printList(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

    # LeetCode problem 26 Swap First and Last (⚡Interview Question). Swap the values of the first and last node
    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return
        temp = self.head.val
        self.head.val = self.tail.val
        self.tail.val = temp

    # LeetCode problem 27 Reverse (⚡Interview Question)
    # Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes
    # the last node, the second node becomes the second-to-last node, and so on.

    def reverse(self):
        temp = self.head
        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev
        self.head, self.tail = self.tail, self.head


newList = LinkedList(5)
newList.append(6)
newList.append(10)
newList.append(7)
newList.append(1)
newList.append(4)
newList.append(2)


newList.printList()
print()
newList.reverse()
print()

newList.printList()
