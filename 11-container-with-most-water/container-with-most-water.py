class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        given an integer array height of length n. There are n vertical lines 
        drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i])
        find two lines that together with the x-axis form a container, such that the 
        container contains the most water
        return maximum amount of water

        greedy:
        two pointers, start from both ends
        min_height from either endpoint is the constraint
        container would be (r - l) * min_height
        increment the pointer that points to the lower height [greedy]
        
        time: O(n), space O(1)
        '''
        l, r = 0, len(height) - 1
        max_container = 0
        while l < r:
            max_container = max(max_container, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_container