class MinStack:

    def __init__(self):
        self.stack = []
        self.min_contenders = []
        
    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_contenders: 
            self.min_contenders.append(value)
            return
        if value <= self.min_contenders[-1]: self.min_contenders.append(value)

    def pop(self) -> None:
        element = self.stack.pop()
        if element == self.min_contenders[-1]: self.min_contenders.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_contenders[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()