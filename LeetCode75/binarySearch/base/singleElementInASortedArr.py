# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid % 2 != 0:
                mid += 1
            if mid == n - 1:
                if nums[mid - 1] != nums[mid]:
                    return nums[mid]
                else:
                    right = mid - 1
            elif mid == 0:
                if nums[mid] != nums[mid + 1]:
                    return nums[mid]
                else:
                    left = mid + 1
            elif nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            elif nums[mid] == nums[mid - 1]:
                right = mid - 1
            elif nums[mid] == nums[mid + 1]:
                left = mid + 1

        return nums[mid]


ob = Solution()
print(ob.singleNonDuplicate([1, 2, 2, 3, 3, 4, 4, 8, 8]))
print(ob.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 8]))
print(ob.singleNonDuplicate([0, 1, 1]))
