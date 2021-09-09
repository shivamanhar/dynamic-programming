class Node:
    def __init__(self, dataval =None):
        self.dataval = dataval
        self.next = None

class LinkedList:
    def __init__(self):
        self.headval = None
    
    def insertEelement(self, data):
        if self.headval is None:
            self.headval = Node(data)
        else:
            node = Node(data)
            self.headval.next = node


example = LinkedList()

for i in range(5):
    a = int(input())
    if example.headval is None:
        example.headval = Node(a)
    else:
        new_node = Node(a)
        example.headval.next = new_node

while example.next is not None:
    print(example.headval.dataval)
    example = example.next

#example.headval = Node(30)
#e2 = Node(90)
#e3 = Node(80)
