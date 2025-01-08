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
        if self.head == None:
            return True
        return False

    def display(self):
        if self.is_empty():
            print("linked list is empty")
        else:
            current_node = self.head
            while current_node != None:
                current_node.display()
                current_node = current_node.next
    
    def add_to_end(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(data)

    def add_to_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_from_front(self):
        if self.is_empty():
            return None
        else:
            deleted_node = self.head
            self.head = self.head.next
            return deleted_node

    def remove_from_back(self):
        if self.is_empty():
            return None
        elif self.head.next == None:
            deleted_node = self.head
            self.head = None
            return deleted_node
        else:
            current_node = self.head
            while current_node.next.next != None:
                current_node = current_node.next
            deleted_node = current_node.next
            current_node.next = None
            return deleted_node

    def delete_by_value(self, value):
        if self.is_empty():
            return None
        elif self.head.data == value:
            return self.remove_from_front()
        else:
            prev_node = self.head
            current_node = prev_node.next
            while current_node != None:
                if current_node.data == value:
                    prev_node.next = current_node.next
                    return current_node
                prev_node = current_node
                current_node = current_node.next
            return None
    
    def count(self):
        count = 0
        if not self.is_empty():
            current_node = self.head
            while current_node != None:
                count += 1
                current_node = current_node.next
        return count

    def update(self, old_data, new_data):
        if self.is_empty():
            print("empty linked list")
        else:
            current_node = self.head
            while current_node != None:
                if current_node.data == old_data:
                    current_node.data = new_data
                current_node = current_node.next

    def search(self, value):
        if self.is_empty():
            return False
        else:
            current_node = self.head
            while current_node != None:
                if current_node.data == value:
                    return True
                current_node = current_node.next
            return False

#main
test_list = LinkedList()
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()

print("Add to end [Mon]")
print("---")
test_list.add_to_end("Mon")
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()

print("Add to end [Tue]")
print("---")
test_list.add_to_end("Tue")
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()

print("Add to front [Sun]")
print("---")
test_list.add_to_front("Sun")
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()

print("Add to end [Wed]")
print("---")
test_list.add_to_end("Wed")
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()

print("Add to end [Thurs]")
print("---")
test_list.add_to_end("Thurs")
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()

print("Add to end [Fri]")
print("---")
test_list.add_to_end("Fri")
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()

target = "Thursday"
print(f"Search for {target}")
print("---")
if test_list.search(target):
    print(f"{target} exists!")
else:
    print(f"{target} not found.")
print()

print("Update Thurs to Thursday")
print("---")
test_list.update("Thurs", "Thursday")
test_list.display()
print()

print(f"Search for {target}")
print("---")
if test_list.search(target):
    print(f"{target} exists!")
else:
    print(f"{target} not found.")
print()

print("Delete_by_value [Sun]: ")
test_list.delete_by_value("Sun").display()
print("---")
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()

print("Delete_by_value [Tue]: ")
test_list.delete_by_value("Tue").display()
print("---")
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()

print("Delete_by_value [Fri]: ")
test_list.delete_by_value("Fri").display()
print("---")
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()

print("Delete from the back: ")
test_list.remove_from_back().display()
print("---")
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()

print("Delete from the front: ")
test_list.remove_from_front().display()
print("---")
test_list.display()
print("Number of nodes: " + str(test_list.count()))
print()