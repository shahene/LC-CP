# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        def reverse_inorder(root):
            nonlocal total
            if not root:
                return
            if root.right:
                reverse_inorder(root.right)
            tmp = root.val
            root.val = root.val + total
            total += tmp

            if root.left:
                reverse_inorder(root.left)
        reverse_inorder(root)
        return root
