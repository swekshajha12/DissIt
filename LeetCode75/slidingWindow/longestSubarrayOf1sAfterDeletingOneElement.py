# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        num_zeroes = 0
        max_res = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeroes += 1

            while num_zeroes > 1:
                if nums[left] == 0:
                    num_zeroes -= 1

                left += 1

            max_res = max(max_res, right - left + 1)

        # If max_length is 0, it means there are no 1's in the array, so return 0.
        # Otherwise, we need to subtract 1 from max_length to account for the removed 0.
        return max(0, max_res - 1)

    def getLongestSubarrayOf1sBruteForce(self, arr):
        zero_count = 0
        max_res = 0
        res = 0
        n = len(arr)

        def get_max_subarray(arr, skip_idx):
            curr_res = 0
            nonlocal res
            for i in range(n):
                if curr_res > res:
                    res = curr_res
                if i == skip_idx:
                    continue
                if arr[i] == 1:
                    curr_res += 1
                elif arr[i] == 0:
                    curr_res = 0
            if curr_res > res:
                res = curr_res
            return res

        for i in range(n):
            if arr[i] == 0:
                zero_count += 1
                val = get_max_subarray(arr, i)
                if val > max_res:
                    max_res = val

        if zero_count == 0:
            return n - 1
        return max_res

    def getlongestSubarrayOf1sOptimised(self, arr):
        num_zeros = 0
        left = 0
        res = 0
        for right in range(len(arr)):
            if arr[right] == 0:
                num_zeros += 1

            while num_zeros > 1:
                if arr[left] == 0:
                    num_zeros -= 1
                left += 1

            res = max(res, right - left)
        return res

    def getlongestSubarrayOf1sforK(self, arr, k):
        left = 0
        num_zeroes = 0
        max_res = float('-inf')
        for right in range(len(arr)):
            if arr[right] == 0:
                num_zeroes += 1

            while num_zeroes > k:
                if arr[left] == 0:
                    num_zeroes -= 1
                left += 1

            max_res = max(max_res, right - left - k + 1)
        return max_res


obj = Solution()
print(obj.longestSubarray([1, 1, 0, 1]))
print(obj.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(obj.getLongestSubarrayOf1sBruteForce([1, 1, 0, 1]))
print(obj.getLongestSubarrayOf1sBruteForce([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(obj.getlongestSubarrayOf1sOptimised([1, 1, 0, 1]))
print(obj.getlongestSubarrayOf1sOptimised([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(obj.getlongestSubarrayOf1sforK([1, 1, 0, 1], 1))
print(obj.getlongestSubarrayOf1sforK([0, 1, 1, 1, 0, 1, 1, 0, 1], 1))
print(obj.getlongestSubarrayOf1sforK([1, 1, 0, 1], 1))
print(obj.getlongestSubarrayOf1sforK([0, 1, 1, 1, 0, 1, 1, 0, 1], 1))
print(obj.getlongestSubarrayOf1sforK([1, 1, 0, 1], 1))
print(obj.getlongestSubarrayOf1sforK([0, 1, 1, 1, 0, 1, 1, 0, 1], 1))
