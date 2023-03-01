# construct quad tree | leetcode 427 | https://leetcode.com/problems/construct-quad-tree/
# recursively call each quad of the grid and check if each quad is uniform or not

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        def checkThisQuad(row, col, n) -> bool:
            for i in range(row, row + n):
                for j in range(col, col + n):
                    if grid[i][j] != grid[row][col]:
                        return False
            return True

        def quadTree(row, col, n):
            if checkThisQuad(row, col, n):
                return Node(grid[row][col], 1, None, None, None, None)
            

            return Node(grid[row][col], 0,
                quadTree(row, col, n//2), 
                quadTree(row, col + n//2, n//2),
                quadTree(row + n//2, col, n//2),
                quadTree(row + n//2, col + n//2, n//2)
            )

        return quadTree(0, 0, len(grid))

