class Queue:
    def __init__(self):
        self.queue = list()

    def queue_item(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False
    
    def size(self):
        return len(self.queue)

    def remove_item(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements left to dequeue")