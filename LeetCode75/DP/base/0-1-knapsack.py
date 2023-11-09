class Knapsack:
    def __init__(self, W, n):
        self.dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    def recursive_sol(self, wt, val, W, n):
        if n == 0 or W == 0:
            return 0
        elif wt[n - 1] <= W:
            return max(val[n - 1] + self.recursive_sol(wt, val, W - wt[n - 1], n - 1),
                       self.recursive_sol(wt, val, W, n - 1))
        elif wt[n - 1] > W:
            return self.recursive_sol(wt, val, W, n - 1)

    def recursion_with_memoization(self, wt, val, W, n):
        if n == 0 or W == 0:
            return 0
        if self.dp[n][W] != -1:
            return self.dp[n][W]
        if wt[n - 1] <= W:
            self.dp[n][W] = max(val[n - 1] + self.recursion_with_memoization(wt, val, W - wt[n - 1], n - 1),
                                self.recursion_with_memoization(wt, val, W, n - 1))
        elif wt[n - 1] > W:
            self.dp[n][W] = self.recursion_with_memoization(wt, val, W, n - 1)

        return self.dp[n][W]


ob = Knapsack(7, 4)
print(ob.recursive_sol([1, 3, 4, 5], [1, 4, 5, 7], 7, 4))
print(ob.recursion_with_memoization([1, 3, 4, 5], [1, 4, 5, 7], 7, 4))
