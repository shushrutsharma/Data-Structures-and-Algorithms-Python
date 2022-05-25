# average of levels in binary tree | leetcode 637 | https://leetcode.com/problems/average-of-levels-in-binary-tree/
# method: (bfs) level order traversal, but instead of appending level to a list, append its average

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        res = []
        Q = []
        
        Q.append(root)
        lQ = len(Q)
        
        while lQ is not 0:
            level = []
            lQ = len(Q)
            for i in range(lQ):
                node = Q.pop(0)
                if node is not None:
                    level.append(node.val)
                    Q.append(node.left)
                    Q.append(node.right)
            if level:
                res.append(sum(level) / len(level))
                
        return res        