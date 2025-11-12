"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        queue = collections.deque([root])
        while queue:
            prev_node = None
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if prev_node:
                    prev_node.next = cur_node
                prev_node = cur_node
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            
        return root
                