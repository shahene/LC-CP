class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        start wide
        calculate area
        strategically move l/r up/down depending on highest bar
        return max area
        O(n) time + O(1) space
        '''
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            cur_area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, cur_area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
                
        return max_area