# n-ary tree postorder traversal | leetcode 590 | https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/
# method: (dfs) postorder traversal is L R N, so iterate through all children and then save node

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: Node):
        self.postTrv = []
        def dfs(root):
            if root is None:
                return None
        
            [dfs(child) for child in root.children]
            self.postTrv.append(root.val)
            
        dfs(root)
        return self.postTrv
        