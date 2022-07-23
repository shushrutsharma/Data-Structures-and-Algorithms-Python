# evaluate boolean binary tree | leetcode 2331 | https://leetcode.com/problems/evaluate-boolean-binary-tree/
# method: dfs, evaluate left and/or right, return node's value

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, node):
        if node.left is None and node.right is None:
            return node.val
        
        if node.val == 2:
            node.val = bool(self.evaluateTree(node.left)) or bool(self.evaluateTree(node.right))
        
        if node.val == 3:
            node.val = bool(self.evaluateTree(node.left)) and bool(self.evaluateTree(node.right))
            
        return node.val
