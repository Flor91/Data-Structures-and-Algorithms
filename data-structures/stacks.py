class Stack:
    def __init__(self):
        self.stack = []
    
    def add(self, dataval):
        "PUSH operation"
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    
    def remove(self):
        "POP operation: Returns it and deletes it"
        if len(self.stack) <= 0:
            return("No elements in the stack")
        else:
            return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]