class Stack:
    def __init__(self):
        self.data = []
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        if self.is_empty():
            return "stack empty"
        else:
            return self.data.pop()
    
    def display(self):
        print(self.data)
    
    def peek(self):
        if self.is_empty():
            return "stack empty"
        else:
            return self.data[-1]
        
stack1 = Stack()
stack1.push('a')
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