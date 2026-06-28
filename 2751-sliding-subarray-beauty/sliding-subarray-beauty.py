class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        beauty = []
        negative_frequency = {}
        l = 0
        total_negative = 0
        for r in range(len(nums)):
            if nums[r] < 0:
                negative_frequency[nums[r]] = negative_frequency.get(nums[r], 0) + 1
                total_negative += 1
            if r >= k - 1:
                if total_negative < x:
                    beauty.append(0)
                else:
                    xth = 0
                    for i in range(-50, 51):
                        if i in negative_frequency: 
                            xth += negative_frequency[i]
                        if xth >= x: 
                            beauty.append(i)
                            break
                if nums[l] in negative_frequency:
                    negative_frequency[nums[l]] -= 1
                    total_negative -= 1
                    if negative_frequency[nums[l]] == 0:
                        del negative_frequency[nums[l]]
                l += 1

        return beauty