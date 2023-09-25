# https://leetcode.com/problems/single-number/description/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dc = {}
        for i in nums:
            if i in dc:
                dc[i] += 1
            else:
                dc[i] = 1
        for key, value in dc.items():
            if value == 1:
                return key

ob = Solution()
print(ob.singleNumber([4,1,2,1,2]))