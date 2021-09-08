class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):        
        if head is None:
            head = Node(data)
            self.tail = head
        else: 
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return head

mylist= Solution()
head=None
b=mylist.insert(head,2) 
c=mylist.insert(b,8)
d=mylist.insert(c,10)
e=mylist.insert(d,12)    
#d=mylist.insert(c,10)    

#mylist.display(b)
obj = c.next.next.next
print(obj.data)	 
