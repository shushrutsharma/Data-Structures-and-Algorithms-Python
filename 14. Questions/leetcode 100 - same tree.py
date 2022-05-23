# same tree | leetcode 100 | https://leetcode.com/problems/same-tree/
# given a root of each of the two trees, check if the trees are the exact same or not
# method: (DFS) inorder traversal to compare left subtree, current node and right subtree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        lResult = self.isSameTree(p.left, q.left)
        nResult = p.val == q.val
        rResult = self.isSameTree(p.right, q.right)

        return lResult and nResult and rResult