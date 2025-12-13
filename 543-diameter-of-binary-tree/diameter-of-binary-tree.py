# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, global_d=0):
        self.global_d = global_d
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recursive_diameter(root)
        return self.global_d - 1
    def recursive_diameter(self, root):
        # get height of left subtree + right subtree + 1
        # save max diameter
        # return height
        if not root: return 0
        leftHeight = self.recursive_diameter(root.left) 
        rightHeight = self.recursive_diameter(root.right)
        diameter = leftHeight + rightHeight + 1
        self.global_d = max(diameter, self.global_d)
        return max(leftHeight, rightHeight) + 1


        