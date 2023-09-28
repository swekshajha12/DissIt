# https://leetcode.com/problems/single-number-ii/
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_dc = {}
        for i in nums:
            if i in freq_dc:
                freq_dc[i] += 1
            else:
                freq_dc[i] = 1
        for key, value in freq_dc.items():
            if value == 1:
                return key

    def singleNumberNext(self, nums: List[int]) -> int:
        return next(num for num, cnt in Counter(nums).items() if cnt == 1)