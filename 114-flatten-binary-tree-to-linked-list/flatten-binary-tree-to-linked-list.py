# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        preorder traversal
        right pointer points to nxt node
        [1, 2, 3, 4, 5, 6]
        
        root = TreeNode(preorder[0])
        root.left = None
        prev_root = None
        for i in range(1, len(preorder)):
            root.right = TreeNode(preorder[i])
            if prev_root:
                root.left = prev_root
            prev_root = root
            root = root.right
        
            

        '''
        
        def preorder_traversal(node, res):
            if not node:
                return
            res.append(node.val)
            preorder_traversal(node.left, res)
            preorder_traversal(node.right, res)
        preorder_arr = []
        preorder_traversal(root, preorder_arr)

        if not root: return
        def preorder(node, preorder_arr, i):
            if not node or i == len(preorder_arr):
                return
            node.left = None
            node.right = TreeNode(preorder_arr[i])
            preorder(node.left, preorder_arr, i + 1)
            preorder(node.right, preorder_arr, i + 1)
        preorder(root, preorder_arr, 1)
        