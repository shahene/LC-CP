class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = set()
        maximum = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = self.exploreSize(grid, r, c, visited)
                maximum = max(maximum, size)
        return maximum
    
    def exploreSize(self, grid, r, c, visited):
        row_inbound = 0 <= r < len(grid)
        col_inbound = 0 <= c < len(grid[0])
        if not row_inbound or not col_inbound: return 0
        if grid[r][c] == 0: return 0
        if (r, c) in visited: return 0
        visited.add((r, c))
        size = 1
        size += self.exploreSize(grid, r + 1, c, visited)
        size += self.exploreSize(grid, r - 1, c, visited)
        size += self.exploreSize(grid, r, c + 1, visited)
        size += self.exploreSize(grid, r, c - 1, visited)
        return size
