class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals: return res
        intervals.sort(key=lambda x:x[0])
        a_start, a_end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            b_start, b_end = intervals[i][0], intervals[i][1]
            if b_start <= a_end:
                a_end = max(b_end, a_end)
            else:
                res.append([a_start, a_end])
                a_start, a_end = intervals[i]
        res.append([a_start, a_end])
        return res
