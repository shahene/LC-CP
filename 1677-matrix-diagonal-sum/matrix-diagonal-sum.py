class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary_c, secondary_c = 0, len(mat[0]) - 1
        total = r = 0
        while primary_c <= len(mat[0]) - 1:
            if primary_c != secondary_c:
                total += mat[r][primary_c]
            total += mat[r][secondary_c]
            r += 1
            secondary_c -= 1
            primary_c += 1
        return total