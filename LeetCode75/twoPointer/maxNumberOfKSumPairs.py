# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75


# This problem can be solved either by using a dictionary or using 2 pointers
# let's see both


from typing import List
from collections import defaultdict


class Solution:
    def maxOperationsUsingDict(self, nums: List[int], k: int) -> int:
        dc = defaultdict(int)
        maxOps = 0
        for num in nums:
            complement = k - num
            if complement in dc and dc[complement] > 0:
                maxOps += 1
                dc[complement] -= 1
            else:
                dc[num] += 1

        return maxOps

    def maxOperationsUsing2pointer(self, nums: List[int], k: int) -> int:
        nums.sort()
        leftP, rightP = 0, len(nums) - 1
        maxOps = 0
        while leftP < rightP:
            if nums[leftP] + nums[rightP] == k:
                maxOps += 1
                leftP += 1
                rightP -= 1
            elif nums[leftP] + nums[rightP] < k:
                leftP += 1
            elif nums[leftP] + nums[rightP] > k:
                rightP -= 1

        return maxOps


ob = Solution()
print(ob.maxOperationsUsingDict([1, 2, 3, 4], 5))
print(ob.maxOperationsUsing2pointer([1, 2, 3, 4], 5))
