class RandomizedSet:

    def __init__(self):
        '''
        removal from list:
        remove from the map in O(1) time - great

        '''
        self.value_map = {}
        self.array = []
    def insert(self, val: int) -> bool:
        if val not in self.value_map:
            self.array.append(val)
            self.value_map[val] = len(self.array) - 1
            return True
        return False
    def remove(self, val: int) -> bool:
        if val not in self.value_map:
            return False

        current_index, end_index = self.value_map[val], len(self.array) - 1
        tmp = self.array[end_index]
        self.array[current_index], self.array[end_index] = self.array[end_index], self.array[current_index]

        deleted_element = self.array.pop()

        self.value_map[tmp] = current_index
        del self.value_map[deleted_element]
        return True


    def getRandom(self) -> int:
        return random.choice(self.array)
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()