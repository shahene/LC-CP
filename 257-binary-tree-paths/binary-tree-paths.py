# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        current_path, output = [], []
        self.binary_tree_recursive(root, current_path, output)
        n_output = []
        for n in output:
            n_output.append('->'.join([str(x) for x in n]))
        return n_output
    def binary_tree_recursive(self, node, current_path, output):
        if not node: return
        current_path.append(node.val)
        if not node.left and not node.right:
            output.append(list(current_path))
        self.binary_tree_recursive(node.left, current_path, output)
        self.binary_tree_recursive(node.right, current_path, output)
        del current_path[-1]