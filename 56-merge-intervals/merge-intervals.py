class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        output = []
        prev_start, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            if cur_start <= prev_end:
                prev_end = max(prev_end, cur_end)
            else:
                output.append([prev_start, prev_end])
                prev_start, prev_end = intervals[i]
        output.append([prev_start, prev_end])
        return output