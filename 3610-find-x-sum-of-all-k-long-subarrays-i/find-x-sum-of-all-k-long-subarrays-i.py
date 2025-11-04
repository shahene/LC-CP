import heapq
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        for i in range(len(ans)):
            min_heap = []
            freq_counter = collections.Counter(nums[i: i + k])
            print(freq_counter)
            heapq.heapify(min_heap)
            for num, count in freq_counter.items():
                heapq.heappush(min_heap, (-count, -num))
            total = 0
            for _ in range(x):
                if min_heap:
                    count, number = heapq.heappop(min_heap)
                    total += (-number * -count)
            ans[i] = total
        return ans