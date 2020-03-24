import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.dll = DoublyLinkedList()

    def enqueue(self, value):
        self.dll.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.dll.head is None:
            return
        self.size -= 1
        return self.dll.remove_from_head()


    def len(self):
        return self.size


"""
Add to tail and remove from from head 
queue is fifo
-> x -> y -> z ->
remove from head, add to tail
"""