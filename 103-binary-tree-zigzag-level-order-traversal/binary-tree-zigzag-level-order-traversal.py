# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root: return output
        queue = collections.deque([root])
        left_right = True
        while queue:
            current_level = collections.deque()
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if left_right:
                    current_level.append(current_node.val)
                else:
                    current_level.appendleft(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            left_right = not left_right
            output.append(list(current_level))
        return output
