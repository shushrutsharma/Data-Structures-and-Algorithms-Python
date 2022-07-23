# find if path exists in a graph | leetcode 1971 | https://leetcode.com/problems/find-if-path-exists-in-graph/
# method: adjacency list, visited and toVisit lists

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # edge case
        if n == 1 and source == destination:
            return True
        
        edgeMap = defaultdict(list)             # adjacency list
        for edge in edges:
            edgeMap[edge[0]].append(edge[1])  
            edgeMap[edge[1]].append(edge[0])
        
        visited = set()                         # set of visited nodes
        toVisit = [edgeMap[source]]             # set of nodes to visit
        
        # while there are nodes to visit
        while toVisit:

            # this node is now visited
            nodes = toVisit.pop()
           
            # for each node in the adjacent nodes 
            for node in nodes:
                if node == destination:
                    return True

                # if node wasn't visited
                # visit its adjacent nodes
                elif node not in visited:
                    visited.add(node)
                    toVisit.append(edgeMap[node])

                # if node was visited
                # do nothing

        # if no more nodes to visit
        # and still no path
        return False
