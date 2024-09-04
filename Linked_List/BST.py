class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BST():
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        newNode = Node(val)

        if self.root is None:
            self.root = newNode
            return True
        else:
            temp = self.root
            while True:
                if newNode.val == temp.val:
                    return False
                if newNode.val < temp.val:
                    if temp.left is None:
                        temp.left = newNode
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = newNode
                        return True
                    temp = temp.right
    def contains(self, val):
        if self.root is None:
            return False
        else:
            temp = self.root
            while temp:
                if val == temp.val:
                    return True
                elif val < temp.val:
                    temp = temp.left
                else:
                    temp = temp.right
            return False
                    
my_tree = BST()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.contains(10))


print('Root:', my_tree.root.val)            
print('Root->Left:', my_tree.root.left.val)        
print('Root->Right:', my_tree.root.right.val) 
