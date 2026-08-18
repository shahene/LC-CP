class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        '''
        time taken to reach target = target - position / speed
        [(0, 1), (3, 3), (5, 1), (8, 4), (10, 2)] => (1s, 1s), (7s, 3s, 2), (12s)
        
        calc time to reach target
        if next time > curernt time:
            current time = next time
            number_fleets += 1
        '''
        number_fleets = 0
        position_speed = sorted([(p, s) for p, s in zip(position, speed)])
        current_time = -math.inf
        for i in range(len(position_speed) - 1, -1, -1):
            p, s = position_speed[i]
            next_time = (target - p) / s
            if next_time > current_time:
                current_time = next_time
                number_fleets += 1
            
        return number_fleets    