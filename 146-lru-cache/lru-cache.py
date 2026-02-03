class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map of key to nodes
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        # initially want left and right connected so we can insert
        # between them
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        '''
        imagine doubly linked list
        to remove node
        just assign its prev to next
        assign next to its prev
        [] => [] => []
        '''
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    def insert(self, node): # want to insert at the right
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            # remove from list, delete from map => remove lru, delete lru
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)