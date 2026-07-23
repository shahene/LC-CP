class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            c = self.count_single_number(i)
            res[i] = c
        return res
    def count_single_number(self, number: int):
        count = 0
        while number:
            count += 1
            number &= number - 1
        return count