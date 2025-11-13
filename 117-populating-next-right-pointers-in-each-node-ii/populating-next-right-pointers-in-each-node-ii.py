"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        queue = collections.deque([root])
        while queue:
            prev_node = None
            for _ in range(len(queue)):
                n = queue.popleft()
                if prev_node:
                    prev_node.next = n
                prev_node = n
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
        return root