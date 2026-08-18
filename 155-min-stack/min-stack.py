class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min:
            self.min.append(value)
            return
        if self.min[-1] >= value:
            self.min.append(value)

    def pop(self) -> None:
        n = self.stack.pop()
        if self.min[-1] == n:
            self.min.pop()
        
        
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()