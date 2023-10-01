# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75


# we'll use sliding window here

from typing import List


class Solution:

    # This solution times out as this has O(n2) time complexity
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if k > n:
            return 0
        max_avg = 0

        if k == n and n == 1:
            return nums[k - 1]

        for i in range(n):
            if i + k <= n:
                sum = 0
                for i in range(i, i + k):
                    sum += nums[i]
                max_avg = max(max_avg, sum / k)
        return max_avg

    def findMaxAverageSlidingWindow(self, nums: List[int], k: int) -> float:
        n = len(nums)
        current_sum = sum(nums[:k])
        max_average = current_sum / k

        for i in range(k, n):
            current_sum = current_sum + nums[i] - nums[i - k]
            max_average = max(max_average, current_sum / k)

        return max_average


ob = Solution()
print(ob.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(ob.findMaxAverage([5], 1))
print(ob.findMaxAverageSlidingWindow([1, 12, -5, -6, 50, 3], 4))
