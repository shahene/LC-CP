class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for n in edges:
            incoming, outgoing = n
            graph[incoming].append(outgoing)
            graph[outgoing].append(incoming)
        stack = [source]
        visited = set()
        while stack:
            current = stack.pop()
            if current == destination: return True
            for n in graph[current]:
                if n not in visited: 
                    stack.append(n)
                    visited.add(n)
        return False
            