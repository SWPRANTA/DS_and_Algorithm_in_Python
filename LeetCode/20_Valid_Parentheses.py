class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self, val=None):
        node = Node(val)
        self.top = node
        self.length = 0

    def push(self, val):
        node = Node(val, self.top)
        self.top = node
        self.length += 1

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


def isValid(stack, s):
    for item in s:
        valinStack = stack.top.val
        print(valinStack)
        if valinStack == '{':
            print(item)
            if item == '}':
                stack.pop()
            else:
                stack.push(item)
        elif valinStack == '}':
            print(item)
            if item == '{':
                stack.pop()
            else:
                stack.push(item)
        elif valinStack == '[':
            print(item)
            if item == ']':
                stack.pop()
            else:
                stack.push(item)
        elif valinStack == ']':
            print(item)
            if item == '[':
                stack.pop()
            else:
                stack.push(item)

        elif valinStack == '(':
            print(item)
            if item == ')':
                stack.pop()
            else:
                stack.push(item)
        elif valinStack == ')':
            print(item)
            if item == '(':
                stack.pop()
            else:
                stack.push(item)

        else:
            break
    stack.printStack()
    if stack.length == 0:
        return True
    else:
        return False


newStack = Stack()

s = "{[()]}"
ans = isValid(newStack, s)
print(ans)