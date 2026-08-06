class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
        input: positive integer n
        output: 2d n * n array w n * n elements in spiral order

        match:
        spiral order, need to establish boundaries and build the array

        edge cases: 0 not included, 1 <= n <= 20

        plan:
        establish top, bottom, left, right boundaries
        current_n = 1
        while top <= bottom and left <= right:
            go from left to right
            for i in range(left, right + 1):
                matrix[top][i] = current_n
                current_n += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = current_n
                current_n += 1
            right -= 1
            
            then right to left [need to check if boundaries are still in correct positions]
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = current_n
                current_n += 1
            bottom += 1

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = current_n
                current_n += 1
            left += 1
        return matrix
        '''

        matrix = [[0] * n for _ in range(n)]
        current_n = 1
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                matrix[top][i] = current_n
                current_n += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = current_n
                current_n += 1
            right -= 1
            if left <= right:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = current_n
                    current_n += 1
            bottom -= 1
            if top <= bottom :
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = current_n
                    current_n += 1
            left += 1
        return matrix

