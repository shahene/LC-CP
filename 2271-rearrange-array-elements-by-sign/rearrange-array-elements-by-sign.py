
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        '''
        divide array into two subparts
        one positive and one negative
        then iterate through the array swappig elements
        '''
        res = [0] * len(nums)
        pos_index, neg_index = 0, 1
        for n in nums:
            if n > 0:
                res[pos_index] = n
                pos_index += 2
            else:
                res[neg_index] = n
                neg_index += 2
        return res
            
            



