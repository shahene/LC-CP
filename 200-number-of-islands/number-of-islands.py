class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited_set = set()
        num_islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue = collections.deque([(r, c)])
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == '1' and (nr, nc) not in visited_set:
                        visited_set.add((nr, nc))
                        queue.append((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited_set:
                    bfs(r, c)
                    visited_set.add((r, c))
                    num_islands += 1
        return num_islands
                    