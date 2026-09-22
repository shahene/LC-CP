class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        '''
        (nums[i] + nums[j] + nums[k]) % d == 0
        nums[k] % d == -(nums[i] + nums[j]) % d
        outer loop to n - 2
        create counter of possible k values (nums[k%d]) for nums[i+2:]
        then inner loop j to n - 1
        subtrat count of nums[j+1] % d -= 1 and get rid of it from possible k vales
        '''
        n = len(nums)
        count = 0
        for i in range(n - 2):
            right = collections.Counter(ith_val % d for ith_val in nums[i + 2:])
            for j in range(i + 1, n - 1):
                needed_remainder = -(nums[i] + nums[j]) % d
                count += right[needed_remainder]
                right[nums[j+1] % d] -= 1
        return count

        
