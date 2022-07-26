# all paths from source to target | leetcode 797 | https://leetcode.com/problems/all-paths-from-source-to-target/
# method: dfs

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        possiblePaths = []
        
        def dfs(node, visited):
            if node == len(graph) - 1:
                possiblePaths.append(visited) 
            
            for neighbour in graph[node]:
                dfs(neighbour, [*visited, node])
             
        dfs(0, [0])
        return possiblePaths
