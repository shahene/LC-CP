class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        pos = True
        first = 1
        for _ in range(1, n + 1):
            if pos:
                res.append(first)
            else:
                res.append(-first)
                first += 1
            pos = not pos
        
        if n % 2 != 0: 
            res.pop()
            res.append(0)
        return res