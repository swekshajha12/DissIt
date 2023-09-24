# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()


# without using sorted function
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    a, b, write_index = m - 1, n - 1, m + n - 1

    while b >= 0:
        if a >= 0 and nums1[a] > nums2[b]:
            nums1[write_index] = nums1[a]
            a -= 1
        else:
            nums1[write_index] = nums2[b]
            b -= 1

        write_index -= 1
    print(nums1)


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
