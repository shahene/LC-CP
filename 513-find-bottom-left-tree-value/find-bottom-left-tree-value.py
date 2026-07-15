# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # find last row
        # return leftmost value -> [queue[0]]
        queue = collections.deque([root])
        level = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            level += 1
        queue = collections.deque([root])
        level_current = 1
        print(level)
        while queue:
            for _ in range(len(queue)):
                if level_current == level:
                    print(queue)
                    return queue[0].val
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            level_current += 1