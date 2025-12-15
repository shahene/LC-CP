# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
    def dfs(self, node, p, q):
        if not node: return 
        leftTree = self.dfs(node.left, p, q)
        rightTree = self.dfs(node.right, p, q)
        if p.val == node.val: return node
        if q.val == node.val: return node
        if leftTree and rightTree: return node
        if leftTree and not rightTree: return leftTree
        if rightTree and not leftTree: return rightTree
