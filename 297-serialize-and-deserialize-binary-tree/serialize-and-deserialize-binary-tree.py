# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.dfs_serialize(root, res)
        return ','.join(res)
    def dfs_serialize(self, root, res):
        if not root: 
            res.append('N')
            return 
        res.append(str(root.val))
        self.dfs_serialize(root.left, res)
        self.dfs_serialize(root.right, res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        self.global_i = [0]
        return self.dfs_deserialize(vals, self.global_i)
    def dfs_deserialize(self, vals, global_i):
        
        if vals[global_i[0]] == 'N':
            global_i[0] += 1
            return None
        node = TreeNode(int(vals[global_i[0]]))
        global_i[0] += 1
        node.left = self.dfs_deserialize(vals, global_i)
        node.right = self.dfs_deserialize(vals, global_i)
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))