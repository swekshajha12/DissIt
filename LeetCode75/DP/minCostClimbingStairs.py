# https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:

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
print(ob.minCostClimbingStairs([10, 15, 20]))
print(ob.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
