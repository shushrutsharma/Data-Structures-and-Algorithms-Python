# rotate image | leetcode 48 | https://leetcode.com/problems/rotate-image/
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# method: transpose + reflection

# testcase 1
# matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# testcase 2
matrix: list[list[int]] = [[5, 1, 9, 11], [2, 4, 8, 10],[13, 3, 6, 7],[15, 14, 12, 16]]

def rotate(matrix: list[list[int]]) -> None:
    n: int = len(matrix)

    # transpose of the matrix
    def transpose(matrix: list[list[int]]) -> None:
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # reflection of the matrix
    def reflect(matrix: list[list[int]]) -> None:
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    transpose(matrix)
    reflect(matrix)

# output
rotate(matrix)
print(matrix)