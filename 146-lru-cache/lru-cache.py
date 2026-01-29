'''
basically, i'd want to keep track of which is the oldest unused element
when it is used, mark it as most recently used
if len(map) > capacity: pop lease recently used

OrderedDiction -> from collections import OrderedDict
Reordering keys dynamically with move_to_end() (useful for FIFO/LIFO access).
Popping items from either end with popitem(last=True/False).

'''

from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ordered_cache = OrderedDict()
    def get(self, key: int) -> int:
        if key in self.ordered_cache:
            self.ordered_cache.move_to_end(key)
            return self.ordered_cache[key]
        return -1 
    def put(self, key:int, value:int) -> None:
        
        self.ordered_cache[key] = value
        self.ordered_cache.move_to_end(key)
        if len(self.ordered_cache) > self.capacity:
            self.ordered_cache.popitem(last=False)
        
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)