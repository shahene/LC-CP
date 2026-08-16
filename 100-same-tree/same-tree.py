# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        UMPIRE
        understand
        input: two binary tree roots: p and q
        output: true or false depending on if the two trees are structurally identical and nodes have the same value

        match:
        dfs 

        plan:
        base case:
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        recurisve step:
        check left and right subtrees of both roots
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        '''
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(q.right, p.right)