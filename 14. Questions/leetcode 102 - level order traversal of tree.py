# binary tree level order traversal | leetcode 102 | https://leetcode.com/problems/binary-tree-level-order-traversal/
# order: from left to right, level by level
# method: breadth first search

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # l to r, level by level
    def levelOrder(self, root):
        res = []
        tempQ = []
        
        # queue to track visits
        tempQ.append(root)
        LtempQ = len(tempQ)
        
        # keep iterating till: 
        # the track queue is empty
        while LtempQ is not 0:
            LtempQ = len(tempQ)
            level = []
            for i in range(LtempQ):
                node = tempQ.pop(0)             # pop this node from queue  (visited)
                if node is not None:
                    level.append(node.val)      # add this node to the level
                    tempQ.append(node.left)     # add left child to queue   (to visit)
                    tempQ.append(node.right)    # add right child to queue  (to visit)
            if len(level) is not 0:
                res.append(level)
        
        return res
        
        