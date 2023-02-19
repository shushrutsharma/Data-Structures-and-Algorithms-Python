# binary tree zigzag level order traversal | leetcode 103 | https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
# use flag to keep track of reversed levels; O(n) because worst case is full level - n/2 elements

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        res = []
        tempQ = []
        zig = False

        # queue to track visits
        tempQ.append(root)
        LtempQ = len(tempQ)
        
        # keep iterating till: 
        # the track queue is empty
        while LtempQ is not 0:
            LtempQ = len(tempQ)
            level = []
            for i in range(LtempQ):
                node = tempQ.pop(0)                 # pop this node from queue  (visited)
                if node is not None:    
                    level.append(node.val)          # add this node to the level
                    tempQ.append(node.left)         # add left child to queue   (to visit)
                    tempQ.append(node.right)        # add right child to queue  (to visit)

            if len(level) is not 0:                 # add level and reverse if zig
                res.append(reversed(level) if zig else level)
                zig = not zig
        
        return res