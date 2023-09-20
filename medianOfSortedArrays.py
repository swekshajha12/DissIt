# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        n = len(nums1)
        if n%2==0:
            return (nums1[n//2]+nums1[n//2-1])/2
        else:
            return nums1[n//2]

ob = Solution()
print(ob.findMedianSortedArrays([1,2], [3,4]))
print(ob.findMedianSortedArrays([1,2], [3,]))
