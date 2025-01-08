class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None]*max_size
        self.front = 0
        self.rear = 0
    
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front
    
    def enqueue(self, data):
        if self.is_full():
            print("cannot enqueue. queue full.")
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = data
    
    def dequeue(self):
        if self.is_empty():
            return "cannot dequeue. queue empty."
        else:
            dequeued_item = self.queue[self.front]
            self.front = (self.front + 1) % self.max_size
            return dequeued_item

    
    def display(self):
        curr_ptr = self.front
        while curr_ptr != self.rear:
            print(self.queue[curr_ptr])
            curr_ptr = (curr_ptr + 1) % self.max_size
    
    def display_raw(self):
        print(self.queue)
        print(self.front, self.rear)


#main
circular_queue = CircularQueue(3)
circular_queue.display_raw()
circular_queue.display()

#insert 1 item
print("Enqueue a:")
circular_queue.enqueue('a')
circular_queue.display_raw()
circular_queue.display()

#insert 1 item
print("Enqueue b:")
circular_queue.enqueue('b')
circular_queue.display_raw()
circular_queue.display()

#delete 1 item
print("Dequeue:")
print("Deleted: " + circular_queue.dequeue())
circular_queue.display_raw()
circular_queue.display()

#delete 1 item
print("Dequeue:")
print("Deleted: " + circular_queue.dequeue())
circular_queue.display_raw()
circular_queue.display()

#delete 1 item
print("Dequeue:")
print("Deleted: " + circular_queue.dequeue())
circular_queue.display_raw()
circular_queue.display()

#insert 1 item
print("Enqueue c:")
circular_queue.enqueue('c')
circular_queue.display_raw()
circular_queue.display()

#insert 1 item
print("Enqueue d:")
circular_queue.enqueue('d')
circular_queue.display_raw()
circular_queue.display()

#insert 1 item
print("Enqueue e:")
circular_queue.enqueue('e')
circular_queue.display_raw()
circular_queue.display()

#insert 1 item
print("Enqueue f:")
circular_queue.enqueue('f')
circular_queue.display_raw()
circular_queue.display()

#delete 1 item
print("Dequeue:")
print("Deleted: " + circular_queue.dequeue())
circular_queue.display_raw()
circular_queue.display()

#insert 1 item
print("Enqueue f:")
circular_queue.enqueue('f')
circular_queue.display_raw()
circular_queue.display()