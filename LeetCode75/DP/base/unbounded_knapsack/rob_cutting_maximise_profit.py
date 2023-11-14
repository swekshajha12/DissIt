# https://www.codingninjas.com/studio/problems/rod-cutting-problem_800284

class Solution:
    def rod_cut(self, length, price, n):
        target = n

        def solve(length, price, target, n):
            if n == 0 or target == 0:
                return 0

            if length[n - 1] <= target:
                return max(price[n - 1] + solve(length, price, target - length[n - 1], n),
                           solve(length, price, target, n - 1))
            else:
                return solve(length, price, target, n - 1)

        return solve(length, price, target, n)

    def tabulisation(self, length, price, n):
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if length[i - 1] <= j:
                    dp[i][j] = max(price[i - 1] + dp[i][j - length[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][n]


ob = Solution()
print(ob.rod_cut([1, 2, 3, 4, 5], [2, 5, 7, 8, 10], 5))
print(ob.tabulisation([1, 2, 3, 4, 5], [2, 5, 7, 8, 10], 5))
