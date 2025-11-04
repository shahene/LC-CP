import heapq
class MinStack:
    def __init__(self):
        self.min_heap = []
        self.stack = []
        

    def push(self, val: int) -> None:
        heapq.heappush(self.min_heap, val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped_el = self.stack.pop()
        x = True
        n_list = []
        while x:
            popped_el_one = heapq.heappop(self.min_heap)
            if popped_el_one == popped_el:
                x = False
            else:
                n_list.append(popped_el_one)
        for i in range(len(n_list)):
            heapq.heappush(self.min_heap, n_list[i])
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_heap[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()