# minimum distance between bst nodes | leetcode 783 | https://leetcode.com/problems/minimum-distance-between-bst-nodes
# dfs; inorder; keep track of last traversed node and check against minimum difference


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        stack = []
        curr = root
        last = None
        minDiff = float("inf")
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                if last is not None:
                    minDiff = min(abs(last.val - curr.val), minDiff)
                last = curr
                curr = curr.right
            else:
                break

        return int(minDiff)

