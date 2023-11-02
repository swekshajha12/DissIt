# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

# we'll use 2 pointer approach here also

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height) - 1
        max_area = 0
        while p1 < p2:
            area = (p2 - p1) * min(height[p1], height[p2])
            if area > max_area:
                max_area = area

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max_area

    def containerWithMostWaterConcise(self, arr):
        left, right = 0, len(arr) - 1
        max_area = float('-inf')
        while left < right:
            max_area = max(max_area, (right - left) * min(arr[left], arr[right]))
            if arr[left] <= arr[right]:
                left += 1
            else:
                right -= 1

        return max_area


ob = Solution()
print(ob.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
