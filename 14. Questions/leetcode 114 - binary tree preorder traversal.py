# binary tree preorder traversal | leetcode 94 | https://leetcode.com/problems/binary-tree-preorder-traversal/
# method: node, left subtree, right subtree recursively

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        travList = []
        
        def traverse(root, travList):
            if root is None:
                return None
                
            travList.append(root.val)           # add this node
            traverse(root.left, travList)       # traverse left subtree and add nodes
            traverse(root.right, travList)      # traverse right subtree and add nodes
            
        traverse(root, travList)
        return travList
