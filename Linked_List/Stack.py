class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class stack:
    def __init__(self, val):
        node = Node(val)
        self.top = node
        self.length = 1

    def push(self, val):
        node = Node(val, self.top)
        self.top = node
        self.length+=1

    def pop(self):
        if self.top is None:
            return
        self.top = self.top.next
        self.length -= 1
    def printStack(self):
        temp = self.top
        while temp:
            print(temp.val)
            temp = temp.next


newStack = stack(23)
newStack.push(12)
newStack.pop()
newStack.pop()
newStack.pop()
newStack.push(555)
newStack.printStack()