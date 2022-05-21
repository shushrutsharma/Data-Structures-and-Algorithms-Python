# balance a bst | leetcode 1382 | https://leetcode.com/problems/balance-a-binary-search-tree/
# given a bst, return a balanced bst
# method: use inorder traversal to make a sorted array, convert sorted array to balanced bst

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # convert sorted array to bst
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        root = TreeNode(val = nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
    
    # in-order traveral gives sorted array
    def inorderTraversal(self, root):
        travList = []
        
        def traverse(root, travList):
            if root is None:
                return None
            
            traverse(root.left, travList)
            travList.append(root.val)
            traverse(root.right, travList)
            
        traverse(root, travList)
        return travList

    # balance a binary search tree
    def balanceBST(self, root):
        return self.sortedArrayToBST(self.inorderTraversal(root))