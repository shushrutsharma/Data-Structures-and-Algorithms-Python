# binary tree paths | leetcode 257 | https://leetcode.com/problems/binary-tree-paths/
# method: (dfs) in-order traversal and at each node, update path. if leaf, append to list of paths.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, path):
            if root is None:
                return

            if root.left is None and root.right is None:
                path += str(root.val)
                self.paths.append(path)
                return

            path += str(root.val) + '->'
            dfs(root.left, path)
            dfs(root.right, path)

        self.paths = []
        dfs(root, "")

        return self.paths

