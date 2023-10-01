# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75


# we'll try to use 2 pointers here to solve the problem


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p1, p2 = 0, 0
        n = len(nums)
        while p1 < n and p2 < n:
            if nums[p1] == 0:
                if nums[p2] != 0:
                    nums[p2], nums[p1] = nums[p1], nums[p2]
                    p1 += 1
                else:
                    p2 += 1

            elif nums[p1] != 0:
                p1 += 1
                p2 += 1
        print(nums)


ob = Solution()
ob.moveZeroes([0, 1, 0, 3, 12])
ob.moveZeroes([1,0])
