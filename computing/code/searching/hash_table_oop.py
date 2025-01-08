class HashTable:
    def __init__(self, max_size):
        self.max_size = max_size
        self.table = [None]*max_size
    
    def hash(self, value):
        return value % self.max_size
    
    def insert(self, value):
        count = 0
        x = self.hash(value)
        while self.table[x] != None:
            if count == self.max_size:
                return "cannot insert"
            x = (x + 1) % self.max_size
            count += 1
        self.table[x] = value

    def search(self, value):
        x = self.hash(value)
        initial = x
        while self.table[x] != value:
            if self.table[x] == None:
                return "not found"
            x = (x + 1) % self.max_size
            if x == initial:
                return "not found"
        return self.table[x]
    