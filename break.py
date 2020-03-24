"""
How do you find and return the middle node of a singly linked list in one pass? 
You do not have access to the length of the list. 
If the list is even, you should return the first of the two "middle" nodes. 
You may not store the nodes in another data structure.
"""

# using two values,
# increment first by one,
# second by two

class Node:

    def __init__(self,value=None, next=None):
        self.value = value
        self.next = next
    
    def link(self, new):
        self.next = new

class LinkedList:

    def __init__(self, node=None):
        self.head = node
    
    def insert(self,value):
        new = Node(value)
        new.link(head)
        self.head = new


def one_pass(ll):
    by_land = None 
    by_sea = None

    if ll == None:
        return "empty list"

    while by_land != None and by_sea != None:
        by_land = ll.next
        by_sea = ll.next.next

        return by_land
        



