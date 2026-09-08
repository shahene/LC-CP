class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.merged_list = []
        self.l_index, self.r_index = 0, 0
        self.bool = True
        while self.l_index < len(self.v1) and self.r_index < len(self.v2):
            if self.bool:
                self.merged_list.append(self.v1[self.l_index])
                self.l_index += 1
            else:
                self.merged_list.append(self.v2[self.r_index])
                self.r_index += 1
            self.bool = not self.bool
        while self.l_index < len(self.v1):
            self.merged_list.append(self.v1[self.l_index])
            self.l_index += 1
        while self.r_index < len(self.v2):
            self.merged_list.append(self.v2[self.r_index])
            self.r_index += 1
        self.global_index = 0

    def next(self) -> int:
        number = self.merged_list[self.global_index]
        self.global_index += 1
        return number
            

    def hasNext(self) -> bool:
        return self.global_index < len(self.merged_list)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())