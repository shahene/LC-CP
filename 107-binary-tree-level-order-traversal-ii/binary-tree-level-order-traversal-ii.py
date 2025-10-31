# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = collections.deque([root])
        output = []
        while queue:
            level_arr = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_arr.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            output.append(level_arr)

        return output[::-1]

