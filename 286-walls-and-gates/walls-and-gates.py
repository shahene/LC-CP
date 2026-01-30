class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        '''
        multi source bfs
        start from gates -> add them all to queue
        level order traversal -> up, down, left, right
        if wall or obstacle, cannot get through, if not in range cannot get through
        if empty room, (meaning not 0 or -1) -> assign value of that cell to 
        min(value of that cell, distance)

        dont return anything
        '''
        visited_set = set()
        queue = collections.deque([])
        rows, cols = len(rooms), len(rooms[0])
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                old_r, old_c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = old_r + dr, old_c + dc
                    if nr in range(rows) and nc in range(cols) and rooms[nr][nc] != -1 and rooms[nr][nc] != 0 and (nr, nc) not in visited_set:
                        rooms[nr][nc] = min(rooms[nr][nc], distance)
                        visited_set.add((nr, nc))
                        queue.append((nr, nc))
        