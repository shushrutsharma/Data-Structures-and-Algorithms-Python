# all elements in two bst | leetcode 1305 | https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# method: dfs, sort

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        elements = []
         
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            elements.append(node.val)
            dfs(node.right)
        
        dfs(root1)
        dfs(root2)
        elements.sort()
        return elements
