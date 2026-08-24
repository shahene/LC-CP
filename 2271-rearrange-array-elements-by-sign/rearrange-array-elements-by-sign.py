
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        '''
        divide array into two subparts
        one positive and one negative
        then iterate through the array swappig elements
        '''
        pos_array, neg_array, res = collections.deque([]), collections.deque([]), []
        for n in nums:
            if n > 0:
                pos_array.append(n)
            else:
                neg_array.append(n)
        pos = True
        p_i, n_i = 0, 0
        while p_i < len(pos_array) or n_i < len(neg_array):
            if pos:
                element = pos_array[p_i]
                p_i += 1

            else:
                element = neg_array[n_i]
                n_i += 1
            res.append(element)
            pos = not pos
        return res

            
            



