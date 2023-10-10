# https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        while left <= right:
            if mid == len(nums) - 1:
                return mid
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            mid = (left + right) // 2

        return mid


ob = Solution()
print(ob.findPeakElement([1, 2, 3, 1]))
print(ob.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(ob.findPeakElement([1]))
print(ob.findPeakElement([1, 2, 3, 4, 5, 6]))
