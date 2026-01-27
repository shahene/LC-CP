class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_islands = 0
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c):
            q = collections.deque([])
            q.append((r, c))
            directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    if row + dr in range(rows) and col + dc in range(cols) and (row + dr, col + dc) not in visited and grid[row + dr][col + dc] == "1":
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    num_islands += 1
        return num_islands