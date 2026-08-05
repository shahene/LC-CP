# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        given the root of a binary tree and an integer targetSum, return all root-to-leaf
        paths where the sum of the node values in the path equals targetSum
        each path should be returned as a list of the node values

        need to backtrack at some poin
        '''
        possible_path = []
        res = []
        def helper(root, targetSum):
            if not root:
                return

            possible_path.append(root.val)
            
            if not root.left and not root.right and targetSum == root.val:
                res.append(tuple(possible_path))
            helper(root.left, targetSum - root.val)
            helper(root.right, targetSum - root.val)
            possible_path.pop()
        helper(root, targetSum)
        for i, n in enumerate(res):
            res[i] = list(n)
        return res