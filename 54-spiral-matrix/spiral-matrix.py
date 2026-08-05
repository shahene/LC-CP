class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        returns [1, 2, 3, 6, 9, 8, 7, 4, 5]

        so need some boundary conditions
        top, bottom, left, right
        while top <= bottom and left <= right
        for i in range(right):
            append matrix[top][i]
        top += 1
        for i in range(bottom):
            append matrix[i][right]
        right -= 1
        for i in range(right, left, -1):
            append matrix[bottom][i]
        bottom -= 1
        for i in range(bottom, top, -1):
            append matrix[i][left]
        left += 1
        '''
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []
        while top <= bottom and left <= right:
            if left > right or top > bottom:
                break
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if left > right or top > bottom:
                break
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right or top > bottom:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if left > right or top > bottom:
                break
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res

