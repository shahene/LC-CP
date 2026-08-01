class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        given row x col grid represneting a map where 1 represents land and 0 represents water
        grid cells are connected horizontally/vertically
        grid is completely surrounded by water and there is exactly one island

        check horizontal vertical 
        only check at land positions
        if water at any horizontal/vertical point, +1 to perimeter
        edge counts as water

        '''
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if val == 1:
                    for dr, dc in directions:
                        new_row, new_col = r + dr, c + dc
                        if new_row not in range(rows) or new_col not in range(cols) or grid[new_row][new_col] == 0:
                            perimeter += 1
        return perimeter