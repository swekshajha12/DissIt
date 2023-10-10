# https://leetcode.com/problems/koko-eating-bananas/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from math import ceil


class Solution:

    def calculateHours(self, piles, k):
        totalHours = 0
        for i in range(len(piles)):
            totalHours += ceil(piles[i] / k)
        return totalHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            totalHours = self.calculateHours(piles, mid)
            if totalHours <= h:
                right = mid - 1
            elif totalHours > h:
                left = mid + 1
        # why not mid?
        return left


ob = Solution()
print(ob.minEatingSpeed([3, 6, 7, 11], 8))
print(ob.minEatingSpeed([30, 11, 23, 4, 20], 5))
print(ob.minEatingSpeed([30, 11, 23, 4, 20], 6))
