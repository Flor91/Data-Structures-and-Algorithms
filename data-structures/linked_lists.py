"""
    Linked list implementation
"""
class Node:
    def __init__(self, dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList:
    def __init__(self):
        self.headval=None
    
    def listprint(self):
        """
            Print the linked list
        """
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def insertAtBegining(self, value):
        """
            Insert a new value at the begining of the list
        """
        new_node = Node(value)
        new_node.nextval = self.headval
        self.headval = new_node
    
    def insertAtEnd(self, value):
        """
            Insert a new value at the end of the list
        """
        new_node = Node(value)
        if self.headval is None:
            self.headval = new_node
            return
        last_node = self.headval

        while(last_node.nextval):
            last_node = last_node.nextval
        
        last_node.nextval = new_node
    
    def insertBetween(self, middle_node, value):
        new_node = Node(value)
        new_node.nextval = middle_node
        middle_node.nextval = new_node

    def removeNode(self, key):
        head = self.headval

        if (head is not None):
            if (head.data == key):
                self.headval = head.next
                head = None
                return

        while (head is not None):
            if head.data == key:
                break
            prev = head
            head = head.next

        if (head == None):
            return

        prev.next = head.next

        head = None

list1 = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list1.listprint()

list1.insertAtBegining("Sun")

list1.insertAtEnd("Thu")