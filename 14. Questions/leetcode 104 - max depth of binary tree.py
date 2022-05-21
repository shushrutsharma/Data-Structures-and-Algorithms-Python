# max depth of binary tree | leetcode 104 | https://leetcode.com/problems/maximum-depth-of-binary-tree/
# given the root of a binary tree, return its maximum depth.
# method: recursively increment left and right count for each new node and return max

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        def findDepth(node):
            if node is None:
                return -1

            ldepth = findDepth(node.left)
            rdepth = findDepth(node.right)

            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1
            
        return findDepth(root) + 1
