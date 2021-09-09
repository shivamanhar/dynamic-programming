class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data
    

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data= nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    def add_first(self, node):
        node.next = self.head
        self.head = node

    
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return 
        for current_node in self:
            pass

        current_node.next = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node=  node.next

        nodes.append("None")
        return "->".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


llist = LinkedList()
llist.add_first(Node("b"))
print(llist)

llist.add_first(Node("x"))
print(llist)

llist.add_last(Node("w"))
print(llist)