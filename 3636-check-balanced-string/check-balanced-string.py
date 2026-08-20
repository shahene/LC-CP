class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum, odd_sum = 0, 0
        for i, n in enumerate(num):
            if i % 2 == 0: 
                even_sum += (ord(n) - ord('0'))
            else:
                odd_sum += (ord(n) - ord('0'))
        return even_sum == odd_sum
