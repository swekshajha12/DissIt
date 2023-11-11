# https://leetcode.com/problems/partition-equal-subset-sum/description/

class Solution:

    def recursive_sol_wrong(self, arr, s1, s2, n):
        if n == 0 and s1 == s2:
            return True
        if n == 0 and s1 != s2:
            return False
        if s1 < s2 or s1 == 0:
            return self.recursive_sol(arr, s1 + arr[n - 1], s2, n - 1) or self.recursive_sol(arr, s1, s2, n - 1)
        else:
            return self.recursive_sol(arr, s1, s2 + arr[n - 1], n - 1) or self.recursive_sol(arr, s1, s2, n - 1)

    def recursive_sol(self, arr):

        def sol_impl(arr, target, n):
            if n == 0 and target != 0:
                return False
            if target == 0:
                return True
            if arr[n - 1] <= target:
                return sol_impl(arr, target - arr[n - 1], n - 1) or sol_impl(arr, target, n - 1)
            else:
                return sol_impl(arr, target, n - 1)

        if sum(arr) % 2 != 0:
            return False
        else:
            return sol_impl(arr, sum(arr) // 2, len(arr))

    # Question: can you think of cases where sum is even but it's not possible to partition them into 2 subset
    # answer: [1,2,5]
    def recursive_with_memoization_sol(self, arr):
        def sol_impl(arr, target, n):
            nonlocal dp
            if n == 0 and target != 0:
                return False
            if target == 0:
                return True

            if dp[n][target] != -1:
                return dp[n][target]

            if arr[n - 1] <= target:
                dp[n][target] = sol_impl(arr, target - arr[n - 1], n - 1) or sol_impl(arr, target, n - 1)
            else:
                dp[n][target] = sol_impl(arr, target, n - 1)

            return dp[n][target]

        if sum(arr) % 2 != 0:
            return False
        else:
            dp = [[-1 for _ in range((sum(arr) // 2) + 1)] for _ in range(len(arr) + 1)]
            return sol_impl(arr, sum(arr) // 2, len(arr))

    def tabulisation_sol(self, arr):

        def sol_impl(arr, target, n):
            nonlocal dp

            for i in range(n + 1):
                dp[i][0] = True

            for j in range(1, target + 1):
                dp[0][j] = False

            for i in range(1, n + 1):
                for j in range(1, target + 1):
                    if arr[i - 1] <= j:
                        dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]

            return dp[n][target]

        if sum(arr) % 2 != 0:
            return False
        else:
            dp = [[False for _ in range((sum(arr) // 2) + 1)] for _ in range(len(arr) + 1)]
            return sol_impl(arr, sum(arr) // 2, len(arr))


ob = Solution()
print(ob.recursive_sol([1, 5, 11, 5]))
print(ob.recursive_with_memoization_sol([42]))
print(ob.tabulisation_sol([1, 5, 11, 5]))
