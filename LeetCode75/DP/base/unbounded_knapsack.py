class Solution:
    def unbounded_kapsack_recursive(self, values, weight, target):

        def solve(val, weight, target, n):
            if n == 0 or target == 0:
                return 0
            if weight[n - 1] <= target:
                return max(
                    (val[n - 1] + solve(val, weight, target - weight[n - 1], n), solve(val, weight, target, n - 1)))
            else:
                return solve(val, weight, target, n - 1)

        return solve(values, weight, target, len(weight))

    def unbounded_knapsack_recursive_memoization(self, values, weight, target):
        dp = [[0 for _ in range(target + 1)] for _ in range(len(weight) + 1)]

        def solve(val, weight, target, n):
            if n == 0 or target == 0:
                return 0

            if dp[n][target] != 0:
                return dp[n][target]

            if weight[n - 1] <= target:
                dp[n][target] = max((val[n - 1] + solve(val, weight, target - weight[n - 1], n)),
                                    solve(val, weight, target, n - 1))
            else:
                dp[n][target] = solve(val, weight, target, n - 1)

            return dp[n][target]

        return solve(values, weight, target, len(weight))

    def unbounded_knapsack_with_tab(self, values, weight, target):
        n = len(weight)
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

        if n == 0 or target == 0:
            return 0

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if weight[i - 1] <= j:
                    dp[i][j] = max(values[i - 1] + dp[i][j - weight[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]


ob = Solution()
print(ob.unbounded_kapsack_recursive([2, 4, 5, 7], [1, 3, 4, 5], 7))
print(ob.unbounded_knapsack_recursive_memoization([1, 4, 5, 7], [1, 3, 4, 5], 7))
print(ob.unbounded_knapsack_with_tab([2, 4, 5, 7], [1, 3, 4, 5], 7))
