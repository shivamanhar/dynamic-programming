class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class LikedList:
    def __init__(self):
        self.head = None
'''

a = Node(10)
a.next = Node(20)
a.next.next = Node(30)
a.next.next.next = Node(50)

while a.next is not None:
    print(a.data)
    a = a.next
    
    

        

