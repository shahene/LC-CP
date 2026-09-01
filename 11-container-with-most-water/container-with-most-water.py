class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        given an integer height of length n
        n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and
        (i, height[i])

        find two lines that together with the x-axis form a container such that the container
        contains the most water
        return maximum amount of water a container can store

        [1, 2, 3, 4, 5]
        l = 0
        r = 4

        input: list of height 
        output: max area of container

        algorithm:
        we can start at both ends of the array
        we can calculate area, keep running track of max area found
        we want pointer that points to the smaller height to move (either left or right)
        greedy like solution with two pointers

        area = (r - l) * min(height[l], height[r])

        O(N) time because we only process the array once
        O(1) constant space
        '''
        l, r = 0, len(height) - 1
        max_area = -math.inf
        while l < r:
            left_height, right_height = height[l], height[r]
            cur_area = (r - l) * min(left_height, right_height)
            max_area = max(max_area, cur_area)
            if left_height < right_height:
                l += 1
            else:
                r -= 1
    
        return max_area