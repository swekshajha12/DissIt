# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

from typing import List


class Solution:
    def check_chunks(self, nums, left, right, target):
        res = -1
        mid = left + (right - left) // 2
        while left <= right:
            if nums[mid] == target:
                res = mid
                break
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            mid = left + (right - left) // 2
        return res

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        left, right = 0, n - 1
        mid = left + (right - left) // 2
        res = -1
        # find the min element index/pivot index
        while left <= right:
            next = (mid + 1) % n
            prev = (mid - 1 + n) % n
            if nums[mid] < nums[prev] and nums[mid] < nums[next]:
                res = mid
                break
            if nums[left] <= nums[mid] and nums[right] >= nums[mid]:
                right = mid - 1
            elif nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[right] >= nums[mid]:
                right = mid - 1
            mid = left + (right - left) // 2
        res = mid

        left_chunk_res = self.check_chunks(nums, 0, res - 1, target)
        right_chunk_res = self.check_chunks(nums, res, n - 1, target)
        if left_chunk_res == -1 and right_chunk_res == -1:
            return -1
        else:
            if left_chunk_res != -1:
                return left_chunk_res
            else:
                return right_chunk_res


ob = Solution()
print(ob.search([4, 5, 6, 7, 0, 1, 2], 0))
print(ob.search([4, 5, 6, 7, 0, 1, 2], 3))
print(ob.search([1], 1))
