class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find where to insert interval
        # insert interval
        # merge rest of intervals
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        prev_beg, prev_end = intervals[0]
        output = []
        print(intervals)
        for i in range(1, len(intervals)):
            n_beg, n_end = intervals[i]
            if n_beg <= prev_end:
                prev_end = max(n_end, prev_end)
            else:
                output.append([prev_beg, prev_end])
                prev_beg, prev_end = n_beg, n_end

        output.append([prev_beg, prev_end])
        return output
        
