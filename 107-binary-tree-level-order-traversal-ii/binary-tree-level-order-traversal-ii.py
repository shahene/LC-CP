# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root: return output
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                n = queue.popleft()
                level.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            output.append(level)
        return list(reversed(output))
