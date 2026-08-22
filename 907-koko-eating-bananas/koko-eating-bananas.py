class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        [30,11,23,4,20], h = 5
        left = 1, right = 30, mid_k = 15
        '''
        left, right = 1, max(piles)
        min_k = math.inf
        while left <= right:
            mid_k = (left + right) // 2
            print(mid_k)
            valid = self.koko_valid(piles, mid_k, h)
            print(valid)
            if valid:
                right = mid_k - 1
                min_k = min(min_k, mid_k)
            else:
                left = mid_k + 1
        return min_k
            



    def koko_valid(self, piles, k, h):
        hours_taken = 0
        for n in piles:
            hours_taken += (math.ceil(n / k))
        return hours_taken <= h
