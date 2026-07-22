class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def hailstone(n):
            steps = 0
            while n != 1:
                if n & 1 == 1:
                    n = (3 * n) + 1
                else:
                    n = n // 2
                steps += 1
            return steps
        
        tuple_arr = []
        for i in range(lo, hi + 1):
            s = hailstone(i)
            tuple_arr.append((s, i))
        tuple_arr.sort(key=lambda x:x[0])
        return tuple_arr[k-1][1]
            