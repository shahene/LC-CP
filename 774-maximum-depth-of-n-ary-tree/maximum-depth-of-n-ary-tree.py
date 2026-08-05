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
        max_height = 0
        if not root:
            return 0
        for n in root.children:
            child_height = self.maxDepth(n)
            max_height = max(max_height, child_height)
        return 1 + max_height
            
        