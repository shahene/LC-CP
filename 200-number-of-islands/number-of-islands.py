class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_r, total_c = len(grid), len(grid[0])
        num_islands = 0
        for r in range(len(grid)):

            for c in range(len(grid[0])):
                print(grid[r][c])
                if grid[r][c] == '1':
                    num_islands += 1
                    self.dfs(grid, r, c, total_r, total_c)
        return num_islands

    def dfs(self, grid, r, c, total_r, total_c):
        if r >= total_r or c >= total_c or r < 0 or c < 0 or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        self.dfs(grid, r - 1, c, total_r, total_c)
        self.dfs(grid, r + 1, c, total_r, total_c)
        self.dfs(grid, r, c + 1, total_r, total_c)
        self.dfs(grid, r, c - 1, total_r, total_c)
