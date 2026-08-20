class Solution:
    def isBalanced(self, num: str) -> bool:
        total_sum = 0
        for i, n in enumerate(num):
            if i % 2 == 0: 
                total_sum += (ord(n) - ord('0'))
            else:
                total_sum -= (ord(n) - ord('0'))
        return total_sum == 0
