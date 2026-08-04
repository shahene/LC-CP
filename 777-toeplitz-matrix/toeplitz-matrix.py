class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        '''
        check if every value is equal to its top left neighbor
        top left indices are (r - 1, c - 1)
        if (r - 1, c - 1) are out of bounds, don't check
        otherwise check for equality * return false early if needed
        return true if false condition not hit
        O(m*n) time and O(1) space
        '''
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                top_row = r - 1
                left_col = c - 1
                if top_row in range(len(matrix)) and left_col in range(len(matrix[0])):
                    if matrix[r][c] != matrix[top_row][left_col]: return False
        return True