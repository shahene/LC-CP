"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
import collections
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        height = 0
        if not root: return 0
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                n = queue.popleft()
                for child in n.children:
                    queue.append(child)
            height += 1
        return height
            
        