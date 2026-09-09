class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.v1_ptr = 0
        self.v2_ptr = 0
        self.v1_turn = True

    def hasNext(self) -> bool:
        return self.v1_ptr < len(self.v1) or self.v2_ptr < len(self.v2)
        

    def next(self) -> int:
        if self.v1_ptr >= len(self.v1): self.v1_turn = False
        if self.v2_ptr >= len(self.v2): self.v1_turn = True

        if self.v1_turn:
            returned_number = self.v1[self.v1_ptr]
            self.v1_ptr += 1
        else:
            returned_number = self.v2[self.v2_ptr]
            self.v2_ptr += 1
        self.v1_turn = not self.v1_turn
        return returned_number

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())