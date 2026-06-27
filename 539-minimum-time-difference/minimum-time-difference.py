class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        '''
        given list of 24 hour clock time points in "HH:MM"
        return minimum minutes difference between any two time-points in the list
        
        we need to standardize HH:MM to minutes since midnight
        need first two digits * 60 = minutes
        last two digits also equals minutes

        sort 
        find min difference from adjacent times
        think about wrap around time which would be:
        how many minutes at midnight index of midnight is 24 hours * 60
        1440 - last time + first time
        '''
        def military_minutes(time):
            time_ = time.split(':')

            hours, minutes = int(time_[0]), int(time_[1])
            total_minutes = (hours * 60) + minutes

            return total_minutes
        
        for i, time in enumerate(timePoints):
            total_minutes = military_minutes(time)
            timePoints[i] = total_minutes
        
        timePoints.sort()

        minimum_difference = math.inf

        for i in range(1, len(timePoints)):
            minimum_difference = min(minimum_difference, timePoints[i] - timePoints[i-1])

        minimum_difference = min(minimum_difference, 1440 - timePoints[-1] + timePoints[0])

        return minimum_difference
       

