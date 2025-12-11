class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight, minLeftRight = [], [0] * len(height), []
        maxLeft_n, maxRight_n = 0, 0
        for i in range(len(height)):
            if i == 0:
                maxLeft.append(0)
            else:
                maxLeft.append(maxLeft_n)
            maxLeft_n = max(maxLeft_n, height[i])
            
        first_iter = True
        for i in range(len(height) - 1, -1, -1):
            if first_iter:
                maxRight[i] = 0
                first_iter = False
            else:
                maxRight[i] = maxRight_n
            print(maxRight_n)
            maxRight_n = max(maxRight_n, height[i])
    
        
        min_lr = []
        for l, r in zip(maxLeft, maxRight):
            minimum_l_r = min(l, r)
            min_lr.append(minimum_l_r)
        total = 0
        for i in range(len(min_lr)):
            wtr_available = min_lr[i] - height[i]
            if wtr_available < 0:
                wtr_available = 0
            total += wtr_available
        return total

