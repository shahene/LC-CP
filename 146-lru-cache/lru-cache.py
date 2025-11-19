from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ordered_map = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.ordered_map:
            return -1
        self.ordered_map.move_to_end(key)
        return self.ordered_map[key]

        

    def put(self, key: int, value: int) -> None:
        self.ordered_map[key] = value
        self.ordered_map.move_to_end(key)
        while len(self.ordered_map) > self.capacity:
            self.ordered_map.popitem(last=False)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)