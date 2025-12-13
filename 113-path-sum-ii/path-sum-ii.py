# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        current_path, all_paths = [], []
        self.path_recursive(root, current_path, all_paths, targetSum)
        return all_paths
    def path_recursive(self, root, current_path, all_paths, targetSum):
        if not root: return
        current_path.append(root.val)
        if not root.left and not root.right and root.val == targetSum:
            all_paths.append(list(current_path))
        else:
            self.path_recursive(root.left, current_path, all_paths, targetSum - root.val)
            self.path_recursive(root.right, current_path, all_paths, targetSum - root.val)
        del current_path[-1]
