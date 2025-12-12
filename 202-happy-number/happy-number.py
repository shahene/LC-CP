class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True 
        fast, slow = n, n
        fast, slow = self.convert_number(self.convert_number(fast)), self.convert_number(slow)
        if slow == 1 or fast == 1: return True
        while fast != slow:
            if slow == 1 or fast == 1:
                return True
            fast = self.convert_number(self.convert_number(fast))
            slow = self.convert_number(slow) 
        return False
    def convert_number(self, n: int) -> int:
        digit_sum = 0
        while n:
            digit_sum += ((n % 10) ** 2)
            n = n // 10
        return digit_sum
    


