# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

from typing import List


class Solution:
    def searchRangeFirst(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1
        res = -1
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res = mid
                if mid == 0 or nums[mid - 1] != target:
                    return res
                else:
                    right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res

    def searchRangeLast(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1
        res = -1
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:

                res = mid
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return res
                else:

                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        elif len(nums) == 1 and nums[0] != target:
            return [-1, -1]
        return [self.searchRangeFirst(nums, target), self.searchRangeLast(nums, target)]

    def occurrenceCount(self, nums, target):
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] == target:
            return 1
        elif len(nums) == 1 and nums[0] != target:
            return 0
        right_res = self.searchRangeLast(nums, target)
        left_res = self.searchRangeFirst(nums, target)
        if left_res >= 0 or right_res >= 0:
            return right_res - left_res + 1

        return 0


ob = Solution()
print(ob.searchRange([5, 7, 8, 8, 8, 10], 8))
print(ob.searchRange([5, 7, 7, 8, 8, 10], 6))
print(ob.searchRange([2, 2], 6))
print(ob.occurrenceCount([5, 7, 8, 8, 8, 10], 8))
print(ob.occurrenceCount([5, 7, 7, 8, 8, 10], 6))
print(ob.occurrenceCount([2, 2], 6))
