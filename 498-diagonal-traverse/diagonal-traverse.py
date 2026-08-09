class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        '''
        different row and col starting for each direction
        
        direction = up right
        up and right as much as possible
        1
        then move col to the right
        direction = down left 
        down and left as much as possible
        2 4
        then move row "down"
        direction = up right
        up and to the right as much as possible
        7 5 3 
        then col cant be moved anymore so move row down
        down and left as much as much as possible
        6 8
        row can't be moved down anymore so move col up
        '''
        res = []
        direction = True
        rows, cols = len(mat), len(mat[0])
        last_valid_row, last_valid_col = 0, 0
        current_row, current_col = 0, 0
        while current_row in range(rows) and current_col in range(cols):
            
            # up right
            if direction:
                iterative_row, iterative_col = current_row, current_col
                while iterative_row in range(rows) and iterative_col in range(cols):
                    res.append(mat[iterative_row][iterative_col])
                    last_valid_row, last_valid_col = iterative_row, iterative_col
                    iterative_row -= 1
                    iterative_col += 1
                if last_valid_col < cols - 1:
                    current_col, current_row = last_valid_col + 1, last_valid_row
                else:
                    current_row, current_col = last_valid_row + 1, last_valid_col
                direction = not direction
            # down left
            else:
                iterative_row, iterative_col = current_row, current_col
                while iterative_row in range(rows) and iterative_col in range(cols):
                    res.append(mat[iterative_row][iterative_col])
                    last_valid_row, last_valid_col = iterative_row, iterative_col
                    iterative_row += 1
                    iterative_col -= 1
                if last_valid_row < rows - 1:
                    current_row, current_col = last_valid_row + 1, last_valid_col
                else:
                    current_col, current_row = last_valid_col + 1, last_valid_row
                direction = not direction                    
        return res 