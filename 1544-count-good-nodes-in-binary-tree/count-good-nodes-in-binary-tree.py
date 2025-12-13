# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        current_path = []
        return self.good_nodes_recursive(root, current_path) 
    def good_nodes_recursive(self, root, current_path):
        if not root: return 0
        good_nodes = 0
        maximum_node = -math.inf
        if current_path: 
            maximum_node = max(current_path)
        if root.val >= maximum_node:
            good_nodes += 1
        print(good_nodes)
        current_path.append(root.val)
        
        good_nodes += self.good_nodes_recursive(root.left, current_path)
        good_nodes += self.good_nodes_recursive(root.right, current_path)
        del current_path[-1]
        return good_nodes