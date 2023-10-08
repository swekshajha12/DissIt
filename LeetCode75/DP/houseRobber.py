# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
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
