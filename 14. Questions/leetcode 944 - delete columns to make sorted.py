# delete columns to make sorted | leetcode 944 | https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n_cols = len(strs[0])
        n_rows = len(strs)
        cols_d = 0

        for col in range(n_cols):
            for row in range(1, n_rows):
                if strs[row][col] < strs[row - 1][col]:
                    cols_d += 1
                    break
        
        return cols_d