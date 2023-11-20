# https://leetcode.com/problems/next-greater-element-ii/description/

from typing import List


class Solution:
    def nextGreaterElement(self, arr):
        # append the arr to itself and start processing answer from mid
        stk, res = [], []
        original_len = len(arr)
        arr.extend(arr)
        updated_len = len(arr)
        for i in range(updated_len - 1, -1, -1):
            if i > original_len - 1:
                while stk and stk[-1] <= arr[i]:
                    stk.pop()
                stk.append(arr[i])
            else:
                while stk and stk[-1] <= arr[i]:
                    stk.pop()

                if stk:
                    res.append(stk[-1])
                else:
                    res.append(-1)
                stk.append(arr[i])
        return res[::-1]

    def nextGreaterElementWrong(self, nums: List[int]) -> List[int]:
        left_stk, right_stk = [], []
        res_left, res_right = [], []
        res = []
        n = len(nums)
        for i in range(n - 1, -1, -1):
            while right_stk and right_stk[-1] <= nums[i]:
                right_stk.pop()

            if right_stk:
                res_right.append(right_stk[-1])
            else:
                res_right.append(-1)
            right_stk.append(nums[i])

        for i in range(n):
            while left_stk and left_stk[-1] <= nums[i]:
                left_stk.pop()

            if left_stk:
                res_left.append(left_stk[-1])
            else:
                res_left.append(-1)
                left_stk.append(nums[i])

        res_right = res_right[::-1]
        for i in range(len(res_right)):
            if res_right[i] == -1 and res_left[i] == -1:
                res.append(-1)
            elif res_right[i] != -1 and res_left[i] == -1:
                res.append(res_right[i])
            elif res_right[i] == -1 and res_left[i] != -1:
                res.append(res_left[i])
            else:
                # give more weightage to right as that is closer
                res.append(res_right[i])
        return res


ob = Solution()
print(ob.nextGreaterElement([1, 2, 1]))
print(ob.nextGreaterElement([1, 2, 3, 4, 3]))
print(ob.nextGreaterElement([5, 4, 3, 2, 1]))
print(ob.nextGreaterElement([1, 1, 1, 1, 1]))
print(ob.nextGreaterElement([1, 5, 3, 6, 8]))
print(ob.nextGreaterElement([1, 2, 3, 2, 1]))
