# unique binary search trees | leetcode 96 | https://leetcode.com/problems/unique-binary-search-trees/
# method: dp, use cached results for subtrees of all possible roots

class Solution:
    def numTrees(self, n: int) -> int:
        # cache of possible trees
        possibleTrees = [1] * (n + 1)
        
        # for each number of nodes
        for numNodes in range(2, n + 1):
            
            # for each possible root
            possibleSubTrees = 0
            for possibleRoot in range(1, numNodes + 1):
                Left = possibleRoot - 1
                Right = numNodes - possibleRoot
                possibleSubTrees += possibleTrees[Left] * possibleTrees[Right]
            possibleTrees[numNodes] = possibleSubTrees
            
        return possibleTrees[n]

