class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum, odd_sum = 0, 0
        for i, n in enumerate(num):
            if i % 2 == 0: 
                even_sum += int(n)
            else:
                odd_sum += int(n)
        return even_sum == odd_sum
