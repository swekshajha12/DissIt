# https://leetcode.com/problems/unique-paths-ii/

from typing import List


# we treat obstacles as 0 and rest as 1 in the dp matrix
# initialising the 0,0 and first row and column are important
# while in the end generating the dp matrix, check if in the original
# matrix the value of the current index is not an obstacle

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

        # first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        # first col
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


ob = Solution()
print(ob.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(ob.uniquePathsWithObstacles([[0, 1], [0, 0]]))
print(ob.uniquePathsWithObstacles([[1, 0]]))
