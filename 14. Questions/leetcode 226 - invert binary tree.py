# invert a binary tree | leetcode 226 | https://leetcode.com/problems/invert-binary-tree/
# method: (dfs) keep recursively swapping left and right subtrees

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):

        def dfs(root):
            if root is None:
                return
            
            if root.left is None and root.right is None:
                return
            
            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return root