# merge two binary trees | leetcode 617 | https://leetcode.com/problems/merge-two-binary-trees/
# method: merge current, then merge left and right

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        if root1 is None and root2 is None:
            return None
        
        curr = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        curr.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        curr.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        
        return curr