class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self, val):
        node = Node(val)
        self.first = self.last = node
        self.length = 1

    def enQueue(self, val):
        node = Node(val)
        if self.last is None:
            self.first = self.last = node
        else:
            self.first.next = node
            self.first = self.first.next
        self.length += 1

    def deQueue(self):
        if self.last:
            self.last = self.last.next
            self.length -= 1

    def printQueue(self):
        temp = self.last
        while temp:
            print(temp.val)
            temp = temp.next


queue = Queue(22)
queue.enQueue(25)
queue.enQueue(78)
queue.printQueue()
print()
queue.deQueue()
queue.deQueue()
queue.deQueue()
queue.deQueue()
queue.enQueue(100)
queue.printQueue()
print(queue.length)
