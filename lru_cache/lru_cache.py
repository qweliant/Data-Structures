from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    
    cache is the dll, and has a kv pair
    are nodes in dict or are dicts in nodes
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = {}
        self.queue = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        
        if key not in self.storage:
            return None

        else:
            # find the key in the DLL and move to the front
            node = self.storage[key]
            self.queue.move_to_front(node)
            return node.value[1]
        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        
        # update valye
        if key in self.storage:
            
            node = self.storage[key]
            node.value = (key, value)
            # most recent
            self.queue.move_to_front(node)
            return 
        
        if len(self.storage) == self.limit:

            del self.storage[self.queue.tail.value[0]]
            self.queue.remove_from_tail()

        # add most recently used

        # print(len(self.storage), key, self.limit)
        self.queue.add_to_head((key, value))
        self.storage[key] = self.queue.head
