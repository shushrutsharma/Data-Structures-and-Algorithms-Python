# leaf-similar trees | leetcode 872 | https://leetcode.com/problems/leaf-similar-trees/
# match the leaves of both trees

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def getLeaves(root):
            if root is None:
                return
            
            getLeaves(root.left)
            if root.left is None and root.right is None:
                self.leaves.append(root.val)
            getLeaves(root.right)
        
        self.leaves = []
        getLeaves(root1)
        leaves1 = self.leaves
        
        self.leaves = []
        getLeaves(root2)
        leaves2 = self.leaves
        
        return leaves1 == leaves2