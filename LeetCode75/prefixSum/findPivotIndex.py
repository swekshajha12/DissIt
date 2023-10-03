# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75


from typing import List


class Solution:

    # This approach is wrong
    def pivotIndexNotRight(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        mid = left + right // 2
        while 0 <= mid <= len(nums) - 1:
            left_sum = sum(nums[:mid])
            right_sum = sum(nums[mid + 1:])
            if left_sum == right_sum:
                return mid
            elif left > right_sum:
                left += 1
            else:
                right -= 1

            mid = (left + right) // 2

        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        for idx, val in enumerate(nums):
            right_sum -= val
            if left_sum == right_sum:
                return idx
            left_sum += val

        return -1


obj = Solution()
print(obj.pivotIndex([1, 7, 3, 6, 5, 6]))
print(obj.pivotIndex([1, 2, 3]))
print(obj.pivotIndex([2, -1, 1]))
print(obj.pivotIndex([2, 1, -1]))
