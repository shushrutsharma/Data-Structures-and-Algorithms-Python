# clone graph | leetcode 133 | https://leetcode.com/problems/clone-graph/
# method: depth first search, recursively add neighbours

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node):
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            duplicate = Node(node.val)
            oldToNew[node] = duplicate
            for neighbour in node.neighbors:
                duplicate.neighbors.append(dfs(neighbour))
                
            return duplicate
        
        return dfs(node) if node else None
