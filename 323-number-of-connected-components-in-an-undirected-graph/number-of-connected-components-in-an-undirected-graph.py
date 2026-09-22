import collections
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = self.build_graph(edges)
        visited = set()
        queue = collections.deque([])
        count = 0
        for node in graph:
            if node not in visited:
                queue.append(node)
                count += 1
                while queue:
                    neighbor = queue.popleft()
                    visited.add(neighbor)
                    for n_node in graph[neighbor]:
                        if n_node not in visited:
                            queue.append(n_node)
                            visited.add(n_node)
        for i in range(n):
            if i not in visited: count += 1               
        return count
    def build_graph(self, edges):
        graph = collections.defaultdict(list)
        for node in edges:
            a, b = node
            graph[a].append(b)
            graph[b].append(a)
        return graph