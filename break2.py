class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None
        self.length = 0

    def check(self, value):
        new = Node(value)
        if self.head is None:
            self.length += 1
            self.head = new
        
        return None if self.head is None else True 

    def insert_at_head(self, value):

        if self.check(value):
            return
        
        head_insert = Node(value)
        head_insert.next = self.head
        self.head = head_insert


    def insert_at_end(self,value):

        new = Node(value)
        if self.head is None:
            self.length += 1
            self.head = new
            return
        
        last_iter = self.head

        while(last_iter.next):
            last_iter = last_iter.next
        self.length += 1
        last_iter.next=new

    def list_print(self):

        link = self.head
        while link is not None:
            print (link.value)
            link = link.next

    """                             flip the switch
    prev = null, next = null

    current node:
    head->next = node1              next = head.next, head->next = prev, prev = next, curr = next

    node1->next = node2             node1->next = head

    node2->next - node3             node2->next = node1

    node3->next = node4             node3->next = node2

    node4->next = node5             node4->next = node3

    node5->next = null              node5->next = node4
    """

    def flip_the_switch(self):

        previous_node = None
        current_node = self.head
        next_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node
        self.head = previous_node



links = LinkedList()
links.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

links.head.next = e2
e2.next = e3

links.insert_at_end("Thu")

links.list_print()

links.flip_the_switch()

print('\n')

links.insert_at_head("Sun")

links.list_print()
