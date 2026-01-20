class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right, min_lr, total = [], [0] * len(height), [], 0
        cur_left_max, cur_right_max = 0, 0
        for i in range(len(height)):
            max_left.append(cur_left_max)
            cur_left_max = max(cur_left_max, height[i])
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = cur_right_max
            cur_right_max = max(cur_right_max, height[i])
        i = 0
        for l, r in zip(max_left, max_right):
            minimum = min(l, r)
            water = minimum - height[i] if minimum - height[i] >= 0 else 0
            i += 1
            min_lr.append(water)
        return sum(min_lr)