import collections
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counter = {}
        l = 0
        for r in range(len(nums)):
            if r >= k - 1:
                for i in range(l, r + 1):
                    number = nums[i]
                    if number not in counter:
                        counter[number] = [0, False]
                    if counter[number][1] == False:
                        counter[number][0] += 1
                        counter[number][1] = True
                for n in counter:
                    counter[n][1] = False
                l += 1
        max_num = -1
        for n in counter:
            if counter[n][0] == 1:
                max_num = max(max_num, n)
        return max_num


    '''
    [3, 9, 2, 1, 7]
    {
        3: 1, 9: 2, 2: 3, 1: 1
        l = 1
        for i in range(2, 3):

    }
    '''
