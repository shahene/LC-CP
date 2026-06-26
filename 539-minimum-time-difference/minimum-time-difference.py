class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        '''
        convert all times to minutes since midnight
        sort -> find min minute difference
        '''
        # conversion to minutes since midnight
        normalized_time = []
        for time in timePoints:
            split_time = time.split(':')
            hour_minute, minute = int(split_time[0]) * 60, int(split_time[1])
            normalized_time.append(hour_minute + minute)
        normalized_time.sort()
        min_time = math.inf
        for i in range(1, len(normalized_time)):
            current_diff = abs(normalized_time[i] - normalized_time[i-1])
            min_time = min(min_time, current_diff)
            
        min_time = min(min_time, 1440 - normalized_time[-1] + normalized_time[0])
        return min_time