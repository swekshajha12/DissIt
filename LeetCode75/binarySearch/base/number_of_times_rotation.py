# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Number of times a sorted array is rotated or finding the minimum element in a rotated sorted array are same questions
# assuming clockwise rotation

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        global mid
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            next = (mid + 1) % n
            prev = (mid - 1 + n) % n

            if nums[next] > nums[mid] and nums[prev] > nums[mid]:
                return mid

            # when array is already sorted, go towards the left side
            # as that will have smaller elements
            if nums[left] <= nums[mid] <= nums[right]:
                right = mid - 1
            # this means left part is sorted
            elif nums[left] <= nums[mid]:
                left = mid + 1
            #  this means right part is sorted
            elif nums[right] >= nums[mid]:
                right = mid - 1

        return mid


ob = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
res = ob.findMin(nums)
print(res)
print(nums[res])
