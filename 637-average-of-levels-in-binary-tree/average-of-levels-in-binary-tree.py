# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        average_array = []
        queue = collections.deque([root])
        while queue:
            level_sum = 0
            counter = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                counter += 1
                level_sum += (node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            average_array.append(level_sum / counter)
        return average_array