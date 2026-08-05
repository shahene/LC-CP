# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot: 
            return True
        if not root or not subRoot: 
            return False
        
        if self.is_equal(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def is_equal(self, tree_one, tree_two):
        if not tree_one and not tree_two:
            return True
        if not tree_one or not tree_two or tree_one.val != tree_two.val:
            return False
        return self.is_equal(tree_one.left, tree_two.left) and self.is_equal(tree_one.right, tree_two.right)

        

