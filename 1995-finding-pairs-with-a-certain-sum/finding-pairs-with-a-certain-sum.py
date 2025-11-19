from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_counter = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        prev_num = self.nums2[index]
        self.nums2_counter[prev_num] -= 1
        self.nums2[index] += val
        self.nums2_counter[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        total = 0
        for n in self.nums1:
            if (tot - n) in self.nums2_counter:
                total += (self.nums2_counter[tot - n])
        return total
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)