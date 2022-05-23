# corresponding node in a clone of the binary tree | leetcode 1379 | https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# return a reference to the same node in a cloned tree
# method: traverse through the original and the cloned tree parallely until the original matches the target

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.clonedTarget = None
        def inorderTraversal(original, cloned):
            if original:
                inorderTraversal(original.left, cloned.left)
                if original is target:
                    self.clonedTarget = cloned
                inorderTraversal(original.right, cloned.right)
        
        inorderTraversal(original, cloned)
        return self.clonedTarget