# increasing order search tree | leetcode 897 | https://leetcode.com/problems/increasing-order-search-tree/
# rearrange a bst with each node having only a right child, and the originally left-most leaf as the new root
# method: inorder traversal to return sorted array, insert all elements as right child (since sorted array)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root):
        self.inorderTrv = []
        def inorder(root):
            if root is None:
                return None
            
            inorder(root.left)
            self.inorderTrv.append(root.val)
            inorder(root.right)
           
        inorder(root)
        newRoot = TreeNode(self.inorderTrv[0])
        toReturn = newRoot
        for x in self.inorderTrv[1:]:
            newRoot.right = TreeNode(x)
            newRoot = newRoot.right
        
        return toReturn