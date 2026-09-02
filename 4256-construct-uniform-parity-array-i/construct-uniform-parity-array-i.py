class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = False
        even = False
        for i in range(len(nums1)):
            if nums1[i] % 2 != 0:
                odd = True
                continue
            for j in range(len(nums1)):
                if j != i and (nums1[i] - nums1[j] % 2) != 0:
                    odd = True
            if not odd: break
        for i in range(len(nums1)):
            if nums1[i] % 2 == 0:
                even = True
                continue
            for j in range(len(nums1)):
                if j != i and nums1[i] - nums1[j] % 2 == 0:
                    even = True
            if not even: break
        return odd or even