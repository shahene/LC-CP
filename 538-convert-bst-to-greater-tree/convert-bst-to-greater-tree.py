# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        def traverseBST(node):
            nonlocal total
            if not node:
                return
            if node.right:
                traverseBST(node.right)
            tmp_node, node.val = node.val, total + node.val
            total += tmp_node
            if node.left:
                traverseBST(node.left)
        traverseBST(root)
        return root