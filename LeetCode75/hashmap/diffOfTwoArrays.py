# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import defaultdict


class Solution:

    # instead of dictionary, could also have used a set
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[], []]
        dc = defaultdict(int)
        for i in nums1:
            dc[i] += 1
        for j in nums2:
            dc[j] += 1

        for key, value in dc.items():
            if key in nums1 and key not in nums2:
                res[0].append(key)
            elif key not in nums1 and key in nums2:
                res[1].append(key)

        return res


obj = Solution()
print(obj.findDifference([1, 2, 3], [2, 4, 6]))
print(obj.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
