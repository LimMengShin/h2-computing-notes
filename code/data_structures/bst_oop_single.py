class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, value):
        new_node = BST(value)
        if value < self.data:
            if self.left == None:
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = new_node
            else:
                self.right.insert(value)
    
    def search(self, value):
        if value == self.data:
            return "found"
        elif value < self.data:
            if self.left == None:
                return "not found"
            else:
                return self.left.search(value)
        else:
            if self.right == None:
                return "not found"
            else:
                return self.right.search(value)
    
    def lookup(self, value, parent=None): #lookup is to return the node to be found and its parent node
        if value == self.data:
            return self, parent
        elif value < self.data:
            if self.left == None:
                return "not found"
            else:
                return self.left.lookup(value, self)
        else:
            if self.right == None:
                return "not found"
            else:
                return self.right.lookup(value, self)
    
    def inorder(self):
        if self.left != None:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right != None:
            self.right.inorder()
    
    def preorder(self):
        print(self.data, end=" ")
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()

    def postorder(self):
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        print(self.data, end=" ")
    
    def minimum(self):
        if self.left == None:
            return self.data
        else:
            return self.left.minimum()

    def maximum(self):
        if self.right == None:
            return self.data
        else:
            return self.right.maximum()