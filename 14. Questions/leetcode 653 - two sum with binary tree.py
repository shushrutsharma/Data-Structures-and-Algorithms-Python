# two sum iv - input is a bst | leetcode 653 | https://leetcode.com/problems/two-sum-iv-input-is-a-bst/submissions/
# method: (dfs) bst inorder traversal gives a sorted array, run array two-sum.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSum(self, nums, target):
        prev = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev:
                return [prev[diff], i]
            prev[num] = i
    
    def dfs(self, root):
        if root is None:
            return
        
        self.dfs(root.left)
        self.trv.append(root.val)
        self.dfs(root.right)
    
    def findTarget(self, root, k):
        self.trv = []
        self.dfs(root)
        return self.twoSum(self.trv, k)
        
        