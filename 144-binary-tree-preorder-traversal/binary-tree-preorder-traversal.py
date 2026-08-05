# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        given root, return preorder traversal
        iterative solution
        visit curr, then left children, then right children

        stack = [1]
        res = [1]

        stack = []
        stack = [4, 5, 7]
    
        stack = [1]
        res = [1]
        stack = []
        stack = [3]
        stack = [3, 2]
        stack = [3]
        res = [1, 2]
        stack = [3, 5, 4]
        stack = [3, 5]
        res = [1, 2, 4]
        stack = [3]
        res = [1, 2, 4, 5]
        stack = [3, 7, 6]
        stack = [3, 7]
        res = [1, 2, 4, 5, 6]
        stack = [3]
        res = [1, 2, 4, 5, 6, 7]
        stack = []
        res = [1, 2, 4, 5, 6, 7, 3]
        stack = [8]
        stack = []
        res = [1, 2, 4, 5, 6, 7, 3, 8]
        stack = [9]
        res = [1, 2, 3, 4, 5, 6, 7, 3, 8, 9]
        while stack:
            n = stack.pop()
            res.append(n.val)
            if n.right:
                stack.append(n.right)

            if n.left:
                stack.append(n.left)


        '''
        if not root: return []
        res = []
        stack = [root]
        while stack:
            n = stack.pop()
            res.append(n.val)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
        return res
        