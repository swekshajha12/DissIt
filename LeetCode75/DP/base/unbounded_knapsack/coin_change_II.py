# https://leetcode.com/problems/coin-change/

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def solve(coins, amount, n):
            if n == 0 and amount == 0:
                return 0
            if n == 0 and amount != 0:
                return float('inf')
            if coins[n - 1] <= amount:
                return min(1 + solve(coins, amount - coins[n - 1], n), solve(coins, amount, n - 1))
            else:
                return solve(coins, amount, n - 1)

        res = solve(coins, amount, len(coins))
        if res == float('inf'):
            return -1
        return res

    def coinChange_memoization(self, coins, amount):
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        def solve(coins, amount, n):
            if n == 0 and amount == 0:
                return 0
            if n == 0 and amount != 0:
                return float('inf')
            if dp[n][amount] != -1:
                return dp[n][amount]

            if coins[n - 1] <= amount:
                dp[n][amount] = min(1 + solve(coins, amount - coins[n - 1], n), solve(coins, amount, n - 1))
            else:
                dp[n][amount] = solve(coins, amount, n - 1)

            return dp[n][amount]

        res = solve(coins, amount, len(coins))
        if res == float('inf'):
            return -1
        return res

    def coinChange_tab(self, coins, amount):
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        for j in range(1, amount + 1):
            dp[0][j] = float('inf')

        #  no idea why we did this
        for j in range(1, amount + 1):
            if j % coins[0] == 0:
                dp[1][j] = j // coins[0]
            else:
                dp[1][j] = float('inf')

        for i in range(2, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        if dp[n][amount] == float('inf'):
            return -1
        return dp[n][amount]


ob = Solution()
print(ob.coinChange([1, 2, 11], 11))
print(ob.coinChange([2], 11))
print(ob.coinChange_memoization([1, 2, 11], 11))
print(ob.coinChange_tab([1, 3, 5], 7))
