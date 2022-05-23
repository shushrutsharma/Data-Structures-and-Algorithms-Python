# balanced bst | leetcode 110 | https://leetcode.com/problems/balance-a-binary-search-tree/
# given a bst, check if it is balanced or not
# method: for each subtree, check if its left and right subtrees and balanced, and return the maxDepth + 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(root):
            if root is None: return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            return [balanced, max(left[1], right[1]) + 1]
        
        return dfs(root)[0]