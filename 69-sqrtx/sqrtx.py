import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            mid_calculated = mid * mid
            if mid_calculated == x:
                return (mid)
            elif mid_calculated > x:
                r = mid - 1
            else:
                l = mid + 1
        # r is the largest intger since (r < l after loop ends) such that r * r <= x
        return (r)
            
        