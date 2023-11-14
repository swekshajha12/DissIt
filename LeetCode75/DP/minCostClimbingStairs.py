# https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:

    def recursive(self, cost):

        def solve(cost, i, n):
            if n == 0 or i >= n:
                return 0
            return cost[i] + min(solve(cost, i + 1, n), solve(cost, i + 2, n))

        return min(solve(cost, 0, len(cost)), solve(cost, 1, len(cost) - 1))

    def recursive_with_memoization(self, cost):
        dp = [0] * (len(cost) + 1)
        dp[0], dp[1] = cost[0], cost[1]

        def solve(cost, i, n):
            if n == 0:
                return cost[i]
            if n < 0 or i >= n:
                return 0
            if dp[i] != 0:
                return dp[i]

            dp[i] = cost[i] + min(solve(cost, i + 1, n), solve(cost, i + 2, n))
            return dp[i]

        return min(solve(cost, 0, len(cost)), solve(cost, 1, len(cost) - 1))

    def tab(self, cost):
        dp = [0] * len(cost)+1
        n = len(cost)
        if n <= 0:
            return 0
        dp[0], dp[1] = cost[0], min(cost[0] + cost[1], cost[1])
        for i in range(2, n):
            dp[i] = min(cost[i] + dp[i - 1], cost[i] + dp[i - 2])

        return dp[n - 1]

    def solve(self, cost: List[int]) -> int:
        n = len(cost) + 1
        cost.append(0)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[0] + cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return dp[n - 1]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.solve(cost), self.solve(cost[1:]))


ob = Solution()
# print(ob.minCostClimbingStairs([10, 15, 20]))
# print(ob.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# print(ob.recursive([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# print(ob.recursive([10, 15, 20]))
print(ob.recursive_with_memoization([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(ob.recursive_with_memoization([1, 100]))
print(ob.recursive_with_memoization([10, 15, 20]))
print(ob.tab([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(ob.tab([10,15,20]))
