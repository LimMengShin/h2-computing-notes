class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
    
    def dequeue(self):
        if self.is_empty():
            return "empty, cannot dequeue"
        else:
            deleted_node = self.head
            self.head = self.head.next
            return deleted_node.data
    
    def display(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

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