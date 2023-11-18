# https://leetcode.com/problems/next-greater-element-i/description/

from typing import List


class Solution:
    def nextGreaterElementOn(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # find pos of elements
        pos, res = [], []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    pos.append(j)

        for i in range(len(nums1)):
            for j in range(pos[i] + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)
        return res

    def nextGreaterElementLogN(self, nums: List[int]) -> List[int]:
        stk = [nums[-1]]
        res = [-1]
        for i in range(len(nums) - 2, -1, -1):
            while stk and stk[-1] < nums[i]:
                stk.pop()

            if stk:
                res.append(stk[-1])
            else:
                res.append(-1)
            stk.append(nums[i])
        return res[::-1]


ob = Solution()
print(ob.nextGreaterElementOn([4, 1, 2], [1, 3, 4, 2]))
print(ob.nextGreaterElementOn([2, 4], [1, 2, 3, 4]))
print(ob.nextGreaterElementOn([4, 1, 2], [1, 2, 3, 4]))
print(ob.nextGreaterElementLogN([1, 0, 3, 4]))
