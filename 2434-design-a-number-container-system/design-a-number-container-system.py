import heapq
class NumberContainers:

    def __init__(self):
        self.num_heap = {}
        self.num_index = {}
        

    def change(self, index: int, number: int) -> None:
        self.num_index[index] = number
        if number not in self.num_heap:
            hp = [index]
            heapq.heapify(hp)
            self.num_heap[number] = hp
        else:
            heapq.heappush(self.num_heap[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_heap: return -1
        hp = self.num_heap[number]
        while hp and self.num_index[hp[0]] != number:
            heapq.heappop(hp)
        return -1 if not hp else hp[0]
        
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)