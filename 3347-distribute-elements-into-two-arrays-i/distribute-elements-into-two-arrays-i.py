class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [], []
        for i, n in enumerate(nums):
            if i == 0: 
                arr1.append(n)
            elif i == 1: 
                arr2.append(n)
            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(n)
                else:
                    arr2.append(n)
        arr1.extend(arr2)
        return arr1

