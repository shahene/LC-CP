import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = collections.Counter(nums)
        min_heap = [(-1 * c, n) for n, c in num_counter.items()]
        heapq.heapify(min_heap)
        output = []
        for _ in range(k):
            count, val = heapq.heappop(min_heap)
            output.append(val)
        return output
