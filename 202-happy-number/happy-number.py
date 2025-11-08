class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        slow, fast = n, n
        slow, fast = self.sum_square(slow), self.sum_square(self.sum_square(fast))
        if slow == 1 or fast == 1: return True
        while slow != fast:
            if slow == 1 or fast == 1:
                return True
            slow, fast = self.sum_square(slow), self.sum_square(self.sum_square(fast))
        return False
    def sum_square(self, number):
        squared_sum = 0
        while number:
            digit = number % 10
            number = number // 10
            squared_sum += (digit ** 2)
        return squared_sum