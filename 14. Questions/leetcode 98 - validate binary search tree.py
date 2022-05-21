# validate binary search tree | leetcode 98 | https://leetcode.com/problems/validate-binary-search-tree/
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# method: in-order traversal of a valid bst gives a sorted array
# tip: use `prev` pointer instead of an array to keep space complexity as O(1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # initialise a prev pointer
    def __init__(self):
        self.prev = None
    
    # in-order traversal (L M R)
    # should return a sorted array
    def isValidBST(self, root) -> bool:
        
        # if this node is none, its a leaf
        if root is None:
            return True
        
        if not self.isValidBST(root.left):
            return False
        
        if self.prev is not None and self.prev.val >= root.val:
            return False
        
        self.prev = root
        
        return self.isValidBST(root.right)