# rotate image | leetcode 48 | https://leetcode.com/problems/rotate-image/
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# method: actual rotation

# testcase 1
# matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# testcase 2
matrix: list[list[int]] = [[5, 1, 9, 11], [2, 4, 8, 10],[13, 3, 6, 7],[15, 14, 12, 16]]

def rotate(matrix: list[list[int]]) -> None:
    n:      int = len(matrix)   # size (n x n)
    left:   int = 0             # left pointer
    right:  int = n - 1         # right pointer
    top:    int = 0             # top pointer
    bottom: int = 0             # bottom pointer
    temp:   int = 0             # temp variable

    # if left pointer is on 
    # the right of the right pointer
    # stop iterating
    while left < right:

        # for each square in layer
        for i in range(right - left):                                
            top:    int = left
            bottom: int = right
            
            temp                        = matrix[top][left + i]     # save top-left
            matrix[top][left + i]       = matrix[bottom - i][left]  # bottom-left to top-left
            matrix[bottom - i][left]    = matrix[bottom][right - i] # bottom-right to bottom-left
            matrix[bottom][right - i]   = matrix[top + i][right]    # top-right to bottom-right
            matrix[top + i][right]      = temp                      # (saved) top-left to top-right

        # next layer
        left  = left + 1                                            
        right = right - 1

# output
rotate(matrix)
print(matrix)