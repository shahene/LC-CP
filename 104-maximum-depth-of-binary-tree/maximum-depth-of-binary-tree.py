# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        m_depth = 1
        return self.max_depth(root, m_depth)
    def max_depth(self, node, m_depth):
        if not node:
            return 0
        return max(self.max_depth(node.left, m_depth) + 1, self.max_depth(node.right, m_depth) + 1)
