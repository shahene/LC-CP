class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        intervals[i] = [start_i, end_i]
        return minimum number of intervals you need to remove to make the rest of the intervals non-overlapping
        
        [[1, 2], [1, 3], [2, 3], [3, 4]]

        returns 1

        b.start < a.end:
            += 1
        else:
            a.end = b.end

        [[1, 2], [1, 2], [1, 2]]
        returns 2

        [[1, 11], [1, 100], [2, 12], [11, 22]]
        '''
        count = 0
        if not intervals: return count
        intervals.sort(key=lambda x: (x[0], x[1]))
        a_end = intervals[0][1]
        for i in range(1, len(intervals)):
            b_start, b_end = intervals[i]
            if b_start < a_end:
                a_end = min(a_end, b_end)
                count += 1
            else:
                a_end = b_end
        return count
        