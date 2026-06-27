class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        '''
        since -50 <= nums[i] <= 50
        we can keep a frequency of all numbers in current_window
        to find xth smallest element, we loop from -50 to 50 
        keep counter until it reaches x
        add that element to res
        move left pointer up, get rid of leftmost element from frequency map

        O(N) time and O(N) space

        [-3,1,2,-3,0,-3]


        '''
        res = []
        l, frequency_map = 0, {}
        total = 0
        for r in range(len(nums)):
            if nums[r] < 0:
                if nums[r] not in frequency_map:
                    frequency_map[nums[r]] = 0
                frequency_map[nums[r]] += 1
                total += 1

            if r >= k - 1:
                count = 0
                if total < x:
                    res.append(0)
                    if nums[l] < 0:
                        frequency_map[nums[l]] -= 1
                        if frequency_map[nums[l]] == 0:
                            del frequency_map[nums[l]]  
                        total -= 1
                    l += 1        
                    continue
                for i in range(-50, 51):
                    if i in frequency_map:
                        count += frequency_map[i]
                    if count >= x:
                        res.append(i)
                        break
                if nums[l] < 0:
                    frequency_map[nums[l]] -= 1
                    if frequency_map[nums[l]] == 0:
                        del frequency_map[nums[l]]  
                    total -= 1
                l += 1               
                
        return res
