# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # COUNT NUMBER OF NODES (SUBTREE)
        # RETURN SUM OF NODES (SUBTREE)
        def count_nodes(node):
            if not root:
                return 0
            left = 0 if not node.left else count_nodes(node.left)
            right = 0 if not node.right else count_nodes(node.right)
            return 1 + left + right
        def sum_values(node):
            if not root:
                return
            left_val = 0 if not node.left else sum_values(node.left)
            right_val = 0 if not node.right else sum_values(node.right)
            return node.val + left_val + right_val
        count = 0
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                number_nodes = count_nodes(node)
                total_val = sum_values(node)
                if total_val // number_nodes == node.val:
                    count += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return count
