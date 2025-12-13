# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def __init__(self, global_v=-math.inf):
        self.global_v = global_v
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_recursion(root)
        return self.global_v
    def max_path_recursion(self, root):
        if not root: return 0
        # with split -> root.val + leftSum + rightSum
        # return without split -> root.val + max(leftSum, rightSum)
        leftSum, rightSum = self.max_path_recursion(root.left), self.max_path_recursion(root.right)
        # ignore negative values
        leftSum, rightSum = max(leftSum, 0), max(rightSum, 0)
        local_sum = max(root.val + leftSum + rightSum, root.val + leftSum, root.val + rightSum)
        self.global_v = max(local_sum, self.global_v)
        return root.val + max(leftSum, rightSum)
