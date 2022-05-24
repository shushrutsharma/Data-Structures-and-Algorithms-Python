# max depth of n-ary tree | leetcode 559 | https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# method: (dfs) return 1 + max(depths) at each node, return 1 if leaf

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        depths = [self.maxDepth(child) for child in root.children]

        if depths:
            return 1 + max(depths)

        return 1