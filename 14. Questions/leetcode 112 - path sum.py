# path sum | leetcode 112 | https://leetcode.com/problems/path-sum/
# given the root of a tree, check if there exists a path whose sum equals target
# method: (dfs) update curSum for each node, and return true or false for each subtree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        
        def dfs(root, curSum):
            if root is None:
                return False
            
            curSum += root.val
            if root.left is None and root.right is None:
                return curSum == targetSum
            
            return dfs(root.left, curSum) or dfs(root.right, curSum)
            
        return dfs(root, 0)
                

