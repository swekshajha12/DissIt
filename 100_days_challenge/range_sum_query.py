# https://leetcode.com/problems/range-sum-query-immutable/description/

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        n = len(self.nums)
        if left == right:
            return self.nums[left]
        if (right - left + 1) % 2 == 0:
            while left <= right:
                res += self.nums[left] + self.nums[right]
                left += 1
                right -= 1
        else:
            while left < right:
                res += self.nums[left] + self.nums[right]
                left += 1
                right -= 1
            res += self.nums[left]
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
