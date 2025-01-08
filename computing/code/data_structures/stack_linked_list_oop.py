class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, item): # add to front
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        return self.head == None
    
    def pop(self): # remove from front
        if self.is_empty():
            return None
        else:
            deleted_node = self.head
            self.head = self.head.next
            return deleted_node.data
    
    def display(self):
        current_node = self.head
        print("top")
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def peek(self):
        if self.is_empty():
            return "empty"
        else:
            return self.head.data

#main
stack1 = Stack()
stack1.push('a')
#print(stack1)

stack1.push('b')
stack1.display()
print("Top: " + stack1.peek())

print("Deleted: " + stack1.pop())
stack1.display()
print()

print("pop 2 more times")
print("----------------------------------------")
print(stack1.pop())
print(stack1.pop())