# https://leetcode.com/problems/unique-paths/description/


class Solution:

    # We'll use recursion to solve this
    # recursive solution is taking too
    # much time for big grids
    def checkPaths(self, p1, p2, m, n):
        if p1 == m - 1 and p2 == n - 1:
            return 1
        if p1 > m - 1 or p2 > n - 1:
            return 0
        return self.checkPaths(p1, p2 + 1, m, n) + self.checkPaths(p1 + 1, p2, m, n)

    # we use dynamic programming for optimised solution
    # Here we start from index 1 and since the first row
    # and the first column will have just one ways to reach
    # Now the value of other box would be equal to the sum of ways to
    # reach there from left and top
    def dpSolution(self, m, n):
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]

    def uniquePaths(self, m: int, n: int) -> int:
        # res = self.checkPaths(0, 0, m, n)
        res = self.dpSolution(m, n)
        return res


ob = Solution()
print(ob.uniquePaths(23, 23))
