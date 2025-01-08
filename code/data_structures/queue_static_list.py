class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.front = 0
        self.rear = -1
        self.queue = [None]*max_size
    
    def is_empty(self):
        return self.rear < self.front
    
    def is_full(self):
        return self.rear == self.max_size-1
    
    def enqueue(self, data):
        if self.is_full():
            print("queue full, cannot enqueue")
        else:
            self.rear += 1
            self.queue[self.rear] = data
    
    def dequeue(self):
        if self.is_empty():
            return "queue empty, cannot dequeue"
        else:
            self.front += 1
            return self.queue[self.front-1]
    
    def printQueue(self):
        if self.is_empty():
            print("queue empty")
        else:
            for i in range(self.front, self.rear+1):
                print(self.queue[i], end=" ")
            print(" ")
    
    def display_raw(self):
        print(self.queue)

#main
queue1 = Queue(3)
queue1.display_raw()
queue1.printQueue()

#insert 1 item
print("Enqueue a:")
queue1.enqueue('a')
queue1.display_raw()
queue1.printQueue()

#insert 1 item
print("Enqueue b:")
queue1.enqueue('b')
queue1.display_raw()
queue1.printQueue()

#delete 1 item
print("Dequeue:")
print("Deleted: " + queue1.dequeue())
queue1.display_raw()
queue1.printQueue()

#delete 1 item
print("Dequeue:")
print("Deleted: " + queue1.dequeue())
queue1.display_raw()
queue1.printQueue()

#delete 1 item
print("Dequeue:")
print("Deleted: " + queue1.dequeue())
queue1.display_raw()
queue1.printQueue()

#insert 1 item
print("Enqueue c:")
queue1.enqueue('c')
queue1.display_raw()
queue1.printQueue()

#insert 1 item
print("Enqueue d:")
queue1.enqueue('d')
queue1.display_raw()
queue1.printQueue()