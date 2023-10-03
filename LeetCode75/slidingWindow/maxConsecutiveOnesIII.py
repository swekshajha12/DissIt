# https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75


# We'll solve this question using a list of list

from typing import List


class Solution:

    # Just no
    def longestOneshackyyyasFxxx(self, nums: List[int], k: int) -> int:

        # create a list of list containing the ones in order
        # like this : [[2,3], [6,8]]
        # where these values represent the indices where we have consecutive ones

        max_val, curr_count = 0, 0
        n = len(nums)
        consec_ones = []
        if k > n:
            return max_val
        else:
            start = None
            for i, val in enumerate(nums):
                if val == 1:
                    if start is None:
                        start = i
                else:
                    if start is not None:
                        consec_ones.append([start, i - 1])
                        start = None
            if start is not None:
                consec_ones.append([start, len(nums) - 1])

        if len(consec_ones) == 0:
            return max_val
        else:
            for i, val in enumerate(consec_ones):
                if i == 0:
                    curr_count = val[1] - val[0] + 1 + min(val[0], k)
                else:
                    curr_count = val[1] - val[0] + 1 + min(val[0] - consec_ones[i - 1][1] - 1, k)

                if curr_count > max_val:
                    max_val = curr_count
        return max_val

    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0

        # iterate over the list
        for right in range(len(nums)):

            # if you find a zero, you flip it
            if nums[right] == 0:
                k -= 1

            # you can flip, till you have utilised whole of k
            # otherwise, you'll have to unflip it
            if k < 0:
                if nums[left] == 0:
                    k += 1

                # regardless of nums left value, you have to increment left to find
                # a better window
                left += 1

        return right - left + 1


obj = Solution()
print(obj.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(obj.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))

