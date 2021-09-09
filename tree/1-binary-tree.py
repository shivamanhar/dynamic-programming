class Node:
    def __init__(self, data):
        self.data =data 
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.data = None

    def add(self, current, data):
        if self.data == None:
            self.data = Node(data)
        else:
            if data < current.data:
                if current.left == None:
                    current.left = Node(data)
                else:
                    self.add(current.left, data)
            else:
                if current.right == None:
                    current.right = Node(data)
                else:
                    self.add(current.right, data)
        
        return self.data


    def visit(self, node):
        print(node.data)

    def preorder(self, current):
        self.visit(current)
        self.preorder(current.left)
        self.preorder(current.right)



start = BST()
node = start.add(start, 7)
node = start.add(node, 3)
node = start.add(node, 8)
#num4 = start.add(num3, 2)

#print(node.left.data)

#print(start.preorder(node))

        
