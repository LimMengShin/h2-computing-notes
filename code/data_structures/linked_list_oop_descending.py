class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def display(self):
        print(self.data)
    
    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def display(self):
        if self.is_empty():
            print("linked list is empty")
        else:
            current_node = self.head
            while current_node != None:
                current_node.display()
                current_node = current_node.next

    def insert(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        elif data > self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = None
            current_node = self.head
            while current_node != None:
                if data > current_node.data:
                    new_node.next = current_node
                    prev_node.next = new_node
                    return
                elif current_node.next == None:
                    current_node.next = new_node
                    return
                else:
                    prev_node = current_node
                    current_node = current_node.next

    def reverse(self):
        current_node = self.head
        previous_node = None

        while current_node:
            next_node = current_node.get_next()  # Get the next node
            current_node.set_next(previous_node)  # Reverse the pointer to the previous node

            # Move down the list
            previous_node = current_node
            current_node = next_node

        # After the loop, previous_node will be the new head
        self.head = previous_node

    def reverse(self, current_node=None):
        if current_node == None:
            current_node = self.head
        
        #base case
        if current_node.next == None:
            self.head = current_node
            return
        
        self.reverse(current_node.next)

        current_node.next.next = current_node
        current_node.next = None

    def reverse(self, current_node=None):
        if current_node == None:
            current_node = self.head
        
        if current_node.next == None:
            self.head = current_node
            return

        self.reverse(current_node.next)
        current_node.next.next = current_node
        current_node.next = None


ll = LinkedList()
ll.insert(1)
ll.insert(45)
ll.insert(5)
ll.insert(16)

ll.insert(179667)
ll.display()
ll.reverse()
ll.display()