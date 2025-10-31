class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        regular 3sum
        conditions:
        if total_sum > target:
            r -= 1
        elif total_sum < target:
            l += 1
        keep track of closest sum to target
        closest_sum = min(closest_sum, abs(target - sum))

        O(n^2) time, O(1) space
        '''
        nums.sort()
        closest_distance = math.inf
        closest_sum = math.inf
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                distance = abs(target - current_sum)
                if current_sum > target:
                    r -= 1
                elif current_sum < target:
                    l += 1
                else:
                    return current_sum
                if distance < closest_distance:
                    closest_distance = distance
                    closest_sum = current_sum
        return closest_sum