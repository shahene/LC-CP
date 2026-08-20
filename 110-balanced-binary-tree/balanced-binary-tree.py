# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        for every node, check its left and right subtrees and find its height
        if difference between left and right subtree heights is greater than 1: return false
        if we exhaust the search and we never hit that case: return true
        '''
        if not root: return True
        leftHeight = self.find_height(root.left)
        rightHeight = self.find_height(root.right)
        if abs(leftHeight - rightHeight) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def find_height(self, node):
        if not node: return 0
        return 1 + max(self.find_height(node.left), self.find_height(node.right))
    