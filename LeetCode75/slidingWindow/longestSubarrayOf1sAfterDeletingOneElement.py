# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        num_zeroes = 0
        max_res =0

        for right in range(len(nums)):
            if nums[right]==0:
                num_zeroes+=1

            while num_zeroes>1:
                if nums[left]==0:
                    num_zeroes-=1

                left+=1

            max_res = max(max_res, right-left+1)

        # If max_length is 0, it means there are no 1's in the array, so return 0.
        # Otherwise, we need to subtract 1 from max_length to account for the removed 0.
        return max(0, max_res-1)


obj = Solution()
# print(obj.longestSubarray([1,1,0,1]))
print(obj.longestSubarray([0,1,1,1,0,1,1,0,1]))




