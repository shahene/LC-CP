# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        current_path, output = [], []
        self.recursive_path_sum(root, targetSum, current_path, output)
        return output
    def recursive_path_sum(self, node, targetSum, current_path, all_paths):
        if not node: return
        current_path.append(node.val)
        if node.val == targetSum and not node.left and not node.right:
            all_paths.append(list(current_path))
        else:
            self.recursive_path_sum(node.left, targetSum - node.val, current_path, all_paths)
            self.recursive_path_sum(node.right, targetSum - node.val, current_path, all_paths)
        del current_path[-1]