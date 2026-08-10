from collections import defaultdict, deque
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        '''
        r + c
        0 + 1 = 1
        1 + 0 = 1
        2 + 0 = 2
        1 + 1 = 2
        0 + 2= 2


        '''
        res = []
        diagonal_traverse = defaultdict(deque)
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                diagonal_traverse[r + c].appendleft(nums[r][c])
        for index in diagonal_traverse:
            res.extend(diagonal_traverse[index])
        return res
