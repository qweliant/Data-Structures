import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.max = 0
    # Insert the given value into the tree
    def insert(self, value):
        
        leaf = BinarySearchTree(value)
        if value < self.value:
            if self.left:
                leaf = self.left.insert(value)
            else:
                self.left = leaf

        # dupe needs reassignment, interesting to consider context for reassignment of same vals
        elif value >= self.value:
            if self.right:
                leaf = self.right.insert(value)
                self.max = value

            else:
                self.right = leaf
                self.max = value
        return leaf
        

        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
    
        if target == self.value:
            return True

        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        self.max = self.value if self.value > self.max else self.max
        return self.max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        if self.left is not None:
            self.left.for_each(cb)

        if self.right is not None:
            self.right.for_each(cb)

        cb(self.value)
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)       
        


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
        queue = Queue() 
        curr = node
        while curr:
            print(curr.value)
            if curr.left:
                queue.enqueue(curr.left)
            if curr.right:
                queue.enqueue(curr.right)
            curr = queue.dequeue()
            


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

    def custom_raise(self):
        if self.left and self.right is None:
            raise ValueError('The tree is empty')




bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

assert bst.contains(4),True

bst.in_order_print(bst)

print('\n\n\n')

bst.bft_print(bst)