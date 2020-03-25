import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):

        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.dll = DoublyLinkedList()

    def push(self, value):

        self.dll.add_to_tail(value)
        self.size +=1
        
    def pop(self):
        if self.dll.head is None:
            return
        self.size -=1
        return self.dll.remove_from_tail()


    def len(self):

        return self.size
        
"""
stack is filo
-> x -> y -> z ->
remove from head, add to head
"""