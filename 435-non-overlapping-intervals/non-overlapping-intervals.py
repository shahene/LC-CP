import math
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        non_overlapping = 0
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        prev_beg, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            n_beg, n_end = intervals[i]
            if n_beg < prev_end:
                prev_end = min(n_end, prev_end)
                non_overlapping += 1
            else:
                prev_beg, prev_end = n_beg, n_end
        return non_overlapping