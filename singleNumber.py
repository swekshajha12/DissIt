# https://leetcode.com/problems/single-number/description/
from functools import reduce
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

    def Xor(self, a, b):
        return a ^ b

    def singleNumberXor(self, nums: List[int]) -> int:
        return reduce(self.Xor, nums)

        # return reduce(lambda total, el: total ^ el, nums)


ob = Solution()
print(ob.singleNumber([4, 1, 2, 1, 2]))
print(ob.singleNumberXor([4, 1, 2, 1, 2]))
