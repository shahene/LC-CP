import collections
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # group diagonals by the sum of their indices
        # iterate through the matrix normally
        # dictionary that has keys as values -> keys will be r + c,values will be lists
        # 0, 1, 2, 3, 4
        # append to res while changing direction
        # return res

        res = []
        rows, cols = len(mat), len(mat[0])
        diagonal_dictionary = collections.defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                index = r + c
                diagonal_dictionary[index].append(mat[r][c])
        
        direction = False
        for index in diagonal_dictionary:
            if direction:
                res.extend(diagonal_dictionary[index])
                direction = not direction
            else:
                res.extend(diagonal_dictionary[index][::-1])
                direction = not direction
        return res