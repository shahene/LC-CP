class RandomizedSet:

    def __init__(self):
        '''
        removal from list:
        remove from the map in O(1) time - great

        '''
        self.value_map = {}
        self.array = []
        self.idx = 0
    def insert(self, val: int) -> bool:
        if val not in self.value_map:
            self.value_map[val] = self.idx
            self.idx += 1
            self.array.append(val)
            return True
        return False
    def remove(self, val: int) -> bool:
        if val not in self.value_map:
            return  False
        del self.value_map[val]
        return True

    def getRandom(self) -> int:
        while True:
            random_number = random.choice(list(self.value_map.keys()))
            if random_number in self.value_map:
                return random_number
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()