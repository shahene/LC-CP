class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
         # if you mod by 10, we get 1s place (right value)
         # 121 / 100 => 1 (rounding down)
         # chopping off: 
         # 121/10 => 12
         # 121%100 = 21, then 21 / 10 => 2
        divide_val = 1
        while x >= 10 * divide_val:
            divide_val  *= 10
        while x:
            right = x % 10
            left = x // divide_val
            
            if left != right: return False

            x = (x % divide_val) // 10
            divide_val = divide_val / 100
        return True
