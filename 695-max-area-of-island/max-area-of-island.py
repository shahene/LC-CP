class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # explore islands with dfs, keeping track of max size
        max_islands = 0
        total_r, total_c = len(grid), len(grid[0])
        for r in range(total_r):
            for c in range(total_c):
                if grid[r][c] == 1:
                    max_islands = max(max_islands, self.dfs_island(grid, r, c, total_r, total_c))
        return max_islands
        return max_islands
    def dfs_island(self, grid, r, c, total_r, total_c):
        if r >= total_r or c >= total_c or r < 0 or c < 0 or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return self.dfs_island(grid, r + 1, c, total_r, total_c) + self.dfs_island(grid, r - 1, c, total_r, total_c) \
        + self.dfs_island(grid, r, c - 1, total_r, total_c) + self.dfs_island(grid, r, c + 1, total_r, total_c) + 1
