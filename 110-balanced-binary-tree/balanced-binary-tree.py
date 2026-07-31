# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        height-balanced = depth never differs by more than one
        find max height of left and right subtrees make sure their abs difference is no greater than 1
        '''
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True
            
        h = abs(height(root.left) - height(root.right))
        if h >= 2: 
            return False


        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        

       