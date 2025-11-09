# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = 0
        if not root: return min_depth
        queue = collections.deque([root])
        while queue:
            min_depth += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if not current_node.left and not current_node.right: return min_depth
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        
        return min_depth