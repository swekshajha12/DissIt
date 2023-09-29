# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max = max(candies)
        res = []
        for candy in candies:
            if candy + extraCandies >= current_max:
                res.append(True)
            else:
                res.append(False)
        return res


ob = Solution()
print(ob.kidsWithCandies([2, 3, 5, 1, 3], 3))
