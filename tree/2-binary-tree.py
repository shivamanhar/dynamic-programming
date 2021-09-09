class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def setData(self, data):
        self.data = data
    
    #get data 
    def getData(self):
        return self.data

    #get left child of a node
    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setInLeftNode(self, data):
        if self.left == None:
            self.left = Node(data)




start = Node(4)
start.setData(2)
print(start.left)
start.setInLeftNode(10)
print(start.left.data)

