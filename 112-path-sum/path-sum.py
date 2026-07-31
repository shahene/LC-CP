# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        given root of a binary & integer targetSum, return true if the tree has a root to leaf path
        such that adding up all the values along the path equals targetSum

        a leaf is a node with no children

        input: root node of binary tree
        output: boolean true if root to leaf path equals target sum

        recurse using dfs
        left first then right

        IMPORTANT: each recursive call has its own stack frame with its own local variables
        if not root.left and not root.right:
            return False
        if targetSum == 0:
            return True
        
        current_target = targetSum - root.val
        hasPathSum(root.left, current_target) or 
        hasPathSum(root.right, current_target)

        O(N) time and O(log N) space (height of the tree for the call stack)

        '''
        if not root: 
            return False
        
        current_target = targetSum - root.val
        if current_target == 0 and not root.left and not root.right:
            return True
        print(current_target)
        return self.hasPathSum(root.left, current_target) or self.hasPathSum(root.right, current_target)