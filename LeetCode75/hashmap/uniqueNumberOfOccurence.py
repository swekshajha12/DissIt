# https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_list = []
        dc = defaultdict(int)
        for i in arr:
            dc[i] += 1

        for num, freq in dc.items():
            if freq in freq_list:
                return False
            freq_list.append(freq)

        return True


obj = Solution()
print(obj.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
print(obj.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
