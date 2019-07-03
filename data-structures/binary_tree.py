class Node:
    # Each node is a tree
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None

    def insert(self, value):
        if self.data:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.data = value
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

tree = Node(5)
tree.insert(2)
tree.insert(10)
tree.insert(8)
tree.printTree()

# prints 2 5 8 10