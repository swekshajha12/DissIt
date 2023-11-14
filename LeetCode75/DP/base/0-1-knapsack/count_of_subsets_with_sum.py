# https://www.codingninjas.com/studio/problems/count-subsets-with-sum-k_3952532

class Solution:
    def __init__(self, target, n):
        self.dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]

    def recursive_sol(self, arr, target, n):
        if n == 0 and target != 0:
            return 0
        if target == 0:
            return 1

        if arr[n - 1] <= target:
            return self.recursive_sol(arr, target - arr[n - 1], n - 1) + self.recursive_sol(arr, target, n - 1)
        else:
            return self.recursive_sol(arr, target, n - 1)

    def recursive_sol_with_memoization(self, arr, target, n):
        if n == 0 and target != 0:
            return 0
        if target == 0:
            return 1
        if self.dp[n][target] != -1:
            return self.dp[n][target]

        if arr[n - 1] <= target:
            self.dp[n][target] = self.recursive_sol(arr, target - arr[n - 1], n - 1) + self.recursive_sol(arr, target,
                                                                                                          n - 1)
        else:
            self.dp[n][target] = self.recursive_sol(arr, target, n - 1)

        return self.dp[n][target]

    def tabulisation_sol(self, arr, target, n):
        dp_tab = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp_tab[i][0] = 1

        for j in range(1, target + 1):
            dp_tab[0][j] = 0

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i - 1] <= j:
                    dp_tab[i][j] = dp_tab[i - 1][j - arr[i - 1]] + dp_tab[i - 1][j]
                else:
                    dp_tab[i][j] = dp_tab[i - 1][j]
        return dp_tab[n][target]


ob = Solution(5, 4)
print(ob.recursive_sol([1, 2, 3, 5], 5, 4))
print(ob.recursive_sol_with_memoization([1, 2, 3, 5], 5, 4))
print(ob.tabulisation_sol([1, 2, 3, 6], 5, 4))
