class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        last_index = len(flowerbed) - 1
        index = 0
        while index < len(flowerbed):
            left_val = 0 if index == 0 else flowerbed[index - 1]
            right_val = 0 if index == last_index else flowerbed[index + 1]
            current_val = flowerbed[index]
            if left_val == 0 and right_val == 0 and current_val == 0:
                n -= 1
                flowerbed[index] = 1
            index += 1
        return n <= 0