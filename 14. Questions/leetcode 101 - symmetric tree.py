# symmetric tree | leetcode 101 | https://leetcode.com/problems/symmetric-tree/
# given the root of a binary tree, check whether it is a mirror of itself 
# method: recursively compare two copies of the same tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        def checkSymm(copy1, copy2):
            if copy1 is None and copy2 is None:
                return True
            if copy1 is None or copy2 is None:
                return False
            
            return (copy1.val == copy2.val) and checkSymm(copy1.left, copy2.right) and checkSymm(copy1.right, copy2.left)
        
        return checkSymm(root, root)
