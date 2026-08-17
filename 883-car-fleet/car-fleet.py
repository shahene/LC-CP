class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        combine two arrays (position and speed)
        sort new array based on position

        number of fleets = 0
        start from right
        calculate time taken to reach target (target - current position) / speed
        if next time is <= current time: 
            continue
        otherwise 
            current time = next time
            fleet += 1

        [(position1, speed1), (position2, speed2)]

        '''
        fleets = 0
        position_speed = [(p, s) for p, s in zip(position, speed)]
        position_speed.sort(key=lambda x: x[0])
        current_time = -math.inf
        for i in range(len(position_speed) - 1, -1 , -1):
            p, s = position_speed[i]
            next_time = (target - p) / s
            if next_time > current_time:
                current_time = next_time
                fleets += 1

        return fleets
        