# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:

    def rob_recursive(self, nums):

        def solve(nums, n):
            if n <= 0:
                return 0
            return max(nums[n - 1] + solve(nums, n - 2), solve(nums, n - 1))

        return solve(nums, len(nums))

    def rob_recursive_memoisation(self, nums):
        dp = [0 for _ in range(len(nums))]

        def solve(nums, n):
            if n <= 0:
                return 0
            if dp[n - 1] != 0:
                return dp[n - 1]
            dp[n - 1] = max(nums[n - 1] + solve(nums, n - 2), solve(nums, n - 1))
            return dp[n - 1]

        return solve(nums, len(nums))

    def rob_tab(self, nums):
        dp = [0 for _ in range(len(nums))]

        def solve(nums, n):
            if n <= 0:
                return 0
            for i in range(n - 1, -1, -1):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            return dp[0]

        return solve(nums, len(nums))

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * len(nums)
        if n < 3:
            return max(nums)
        else:
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[n - 1]


ob = Solution()
print(ob.rob([1, 2, 3, 1]))
print(ob.rob_recursive([1, 2, 3, 1]))
print(ob.rob_recursive_memoisation([1, 2, 3, 1]))
print(ob.rob_tab([1, 2, 3, 1]))
