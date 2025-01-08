class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.max_size-1

    def push(self, item):
        if self.is_full():
            print("stack full. cannot add.")
        else:
            self.top += 1
            self.stack[self.top] = item
    
    def pop(self):
        if self.is_empty():
            return "stack empty. cannot pop."
        else:
            self.top -= 1
            return self.stack[self.top+1]

    def peek(self):
        if self.is_empty():
            return "stack empty. cannot peek."
        else:
            return self.stack[self.top]
    
    def display(self):
        if self.is_empty():
            return "stack empty"
        else:
            return self.stack[:self.top+1]

    def display_raw_array(self):
        print(self.stack)

# Main
new_stack = Stack(3)
print("Display:", new_stack.display())
print()

new_stack.push("apple")
print("Display:", new_stack.display())
print("Peek: ", new_stack.peek())
print()

print("Popped item:", new_stack.pop())
print("Display:", new_stack.display())
print("Peek: ", new_stack.peek())
print()

print("Popped item:", new_stack.pop())
print("Display:", new_stack.display())
new_stack.display_raw_array()
print()

new_stack.push("pear")
new_stack.push("grapes")
new_stack.push("orange")
new_stack.push("berry")
print("Display:", new_stack.display())
print("Popped item:", new_stack.pop())
print("Display:", new_stack.display())
print("Peek: ", new_stack.peek())
new_stack.display_raw_array()