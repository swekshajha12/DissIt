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


    # this is wrong, for tabulisation db array, try to do it
    # from start to end
    def rob_tab(self, nums):
        dp = [0 for _ in range(len(nums))]

        def solve(nums, n):
            if n <= 0:
                return 0
            for i in range(n - 1, -1, -1):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            print(dp)
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

    def rob_recursive_k(self, nums, k):
        def solve(nums, n):
            if n <= 0:
                return 0
            return max(nums[n - 1] + solve(nums, n - 1 - k), solve(nums, n - 1))

        return solve(nums, len(nums))

    def rob_recursive_with_memoization_k(self, nums, k):
        dp = [float('-inf')] * len(nums)

        def solve(nums, n):
            if n <= 0:
                return 0
            if dp[n - 1] != float('-inf'):
                return dp[n - 1]
            dp[n - 1] = max(nums[n - 1] + solve(nums, n - 1 - k), solve(nums, n - 1))
            return dp[n - 1]

        return solve(nums, len(nums))

    def rob_recursive_tab_k(self, nums, k):
        n = len(nums)
        dp = [0] * len(nums)
        max_till_now = float('-inf')
        if n <= 0:
            return 0
        dp[0]=nums[0]
        for i in range(1,k):
            max_till_now = max(nums[i], max_till_now)
            dp[i]=max_till_now

        for i in range(k, len(nums)):
            dp[i] = max(nums[i] + dp[i - k-1], dp[i-1])
        print(dp)
        return dp[n-1]


ob = Solution()
# print(ob.rob([1, 2, 3, 1]))
# print(ob.rob_recursive([1, 2, 3, 1]))
# print(ob.rob_recursive_k([1, 2, 3, 1], 2))
print(ob.rob_recursive_with_memoization_k([1, 2, 3, 1, 5], 1))
print(ob.rob_recursive_tab_k([1, 2, -3, -1, 5], 1))
# print(ob.rob_recursive_memoisation([1, 2, 3, 1]))
print(ob.rob_tab([1, 2, 3, 1,5]))
