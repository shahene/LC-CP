# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        input: root of a binary tree
        output: int (maximum depth of binary tree)

        recursively pass through the tree's left and right subtrees
        base case: return 1
        return max(left, right)
        '''
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1