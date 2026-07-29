class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        minimum_consecutive = float('inf')
        count_whites = 0
        num_blacks = 0
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                count_whites += 1
            num_blacks += 1
            if num_blacks == k:
                minimum_consecutive = min(minimum_consecutive, count_whites)
            while num_blacks >= k:
                if blocks[l] == 'W':
                    count_whites -= 1
                l += 1
                num_blacks -= 1
        return minimum_consecutive
