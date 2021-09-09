from typing import NewType


class Node:
    def __init__(self, data= None):
        self.item = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.start_node = None
    
    def insertToEmptyList(self, data):
        if self.start_node  is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")

    def insertToEnd(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    # Delete the elements from the start
    def deleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return

        self.start_node = self.start_node.next
        self.start_prev = None

    # Delete the elements from the end
    def delete_at_end(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node =None
            return 
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
    
    # Traversing and Displaying each element of the list
    def display(self):
        if self.start_node is None:
            print("The list is empty")
        else:
            n = self.start_node
            while n is not None:
                print("Element is:", n.item)
                n = n.next
        print("\n")
    

# Create a new Double Linked List
NewDoublyLinkedList = DoubleLinkedList()
# Insert the element to empty list
NewDoublyLinkedList.insertToEmptyList(10)
NewDoublyLinkedList.insertToEnd(34)
NewDoublyLinkedList.insertToEnd(36)
NewDoublyLinkedList.insertToEnd(41)
NewDoublyLinkedList.insertToEnd(40)

NewDoublyLinkedList.display()

NewDoublyLinkedList.deleteAtStart()
NewDoublyLinkedList.display()
NewDoublyLinkedList.delete_at_end()

NewDoublyLinkedList.display()


