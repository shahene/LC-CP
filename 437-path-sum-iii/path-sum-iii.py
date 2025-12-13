# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        current_path = []
        return self.path_sum_recursive(root, current_path, targetSum)
    def path_sum_recursive(self, root, current_path, targetSum):
        if not root: return 0
        path_sum, path_count = 0, 0
        current_path.append(root.val)
        for i in range(len(current_path) -1, -1, -1):
            path_sum += current_path[i]
            if path_sum == targetSum:
                path_count += 1
        path_count += self.path_sum_recursive(root.left, current_path, targetSum)
        path_count += self.path_sum_recursive(root.right, current_path, targetSum)
        del current_path[-1]
        return path_count