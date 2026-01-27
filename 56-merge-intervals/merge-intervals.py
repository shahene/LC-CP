class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        intervals[i] = [start_i, end_i]
        merge all overlapping intervals
        return an array of non-overlapping intervals

        sort intervals by start time
        initial_interval_start
        next end time <= prev_start time:
            if true: need to merge -> merged_interval =[prev_start, max(next end, prev_end)]
            if not: we merge current interval we have to the array
        at the end, we have 1 more left over, just append to merged interval array
        O(nlogn), auxiliary space -> O(1) 
        '''
        merged_intervals = []
        intervals.sort()
        prev_start, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            if cur_start <= prev_end:
                prev_end = max(prev_end, cur_end)
                print(prev_start, prev_end)
            else:
                merged_intervals.append([prev_start, prev_end])
                prev_start, prev_end = intervals[i]
            
        merged_intervals.append([prev_start, prev_end])
        return merged_intervals

        return mered_intervals