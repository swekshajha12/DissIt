# subset sum is a variation of knapsack

class Solution:
    def __init__(self, n, k):
        self.dp = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

    def subset_sum_recursive(self, arr, target, n):
        if n == 0 and target != 0:
            return False
        if target == 0:
            return True

        if arr[n - 1] <= target:
            return self.subset_sum_recursive(arr, target - arr[n - 1], n - 1) or self.subset_sum_recursive(arr, target,
                                                                                                           n - 1)
        else:
            return self.subset_sum_recursive(arr, target, n - 1)

    def subset_sum_recursive_with_memoization(self, arr, target, n):
        if n == 0 and target != 0:
            return False
        if target == 0:
            return True

        if self.dp[n][target] != -1:
            return self.dp[n][target]

        if arr[n - 1] <= target:
            self.dp[n][target] = self.subset_sum_recursive_with_memoization(arr, target - arr[n - 1],
                                                                            n - 1) or self.subset_sum_recursive_with_memoization(
                arr, target,
                n - 1)
        else:
            self.dp[n][target] = self.subset_sum_recursive_with_memoization(arr, target, n - 1)

        return self.dp[n][target]

    # todo : This is not working for all the  test cases, check what's wrong
    def subset_sum_tabulisation(self, arr, target, n):
        dp_tab = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        dp_tab[0][0] = True
        for i in range(n + 1):
            dp_tab[i][0] = True

        for j in range(1, target + 1):
            dp_tab[0][j] = False

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i - 1] <= j:
                    dp_tab[i][j] = dp_tab[i-1][j - arr[i - 1]] or dp_tab[i - 1][j]
                else:
                    dp_tab[i][j] = dp_tab[i - 1][j]

        return dp_tab[n][target]


ob = Solution(5, 11)
print(ob.subset_sum_recursive([2, 3, 7, 8, 10], 11, 5))
print(ob.subset_sum_recursive_with_memoization([2, 3, 7, 8, 10], 11, 5))
print(ob.subset_sum_tabulisation([2, 6, 7, 8, 10], 5, 5))

