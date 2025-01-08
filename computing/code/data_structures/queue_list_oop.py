class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)

    def is_empty(self):
        return self.queue == []
    
    def dequeue(self):
        if self.is_empty():
            return "queue empty"
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

#main
queue1 = Queue()

#display
queue1.display()

#insert 1 item
queue1.enqueue('a')

#display
queue1.display()

#insert 1 item
queue1.enqueue('b')

#display
queue1.display()

#delete 1 item
print("Deleted: " + queue1.dequeue())

#display
queue1.display()

#delete 2 more items
print("Deleted: " + queue1.dequeue())
print("Deleted: " + queue1.dequeue())

#display
queue1.display()