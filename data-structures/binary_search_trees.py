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

    def search_value(self, value):
        """ 
            Search for a value in the tree.
            Searching for a value in a tree involves comparing the incoming value with the value exiting nodes. 
            Here also we traverse the nodes from left to right and then finally with the parent. 
            If the searched for value does not match any of the exitign value, then we return not found message else the found message is returned.
        """
        if value < self.data:
            if self.left is None:
                return str(value) + " Value not found"
            return self.left.search_value(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " Value not found"
            return self.right.search_value(value)
        else:
            return str(value) + " Value found"
    
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