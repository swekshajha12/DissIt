# https://leetcode.com/problems/range-sum-query-2d-immutable/description/

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rows, cols = len(self.matrix), len(self.matrix[0])
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        if rows == 0 and cols == 0:
            return 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                dp[i][j] = self.matrix[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
        return dp[row2 + 1][col2 + 1] - dp[row1][col2 + 1] - dp[row2 + 1][col1] + dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
param_1 = numMatrix.sumRegion(2, 1, 4, 3)
print(param_1)
