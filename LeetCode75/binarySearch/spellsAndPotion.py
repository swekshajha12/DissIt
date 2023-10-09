# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # n log n

        res = []

        for i in range(len(spells)):
            left, right = 0, len(potions) - 1
            mid = left + right // 2
            count=0
            while left <= right:
                if potions[mid]*spells[i] >= success:
                    count+=right-mid+1
                    right = mid - 1
                else:
                    left = mid + 1
                mid = (left + right) // 2
            res.append(count)

        return res


ob = Solution()
print(ob.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
print(ob.successfulPairs([3], [1, 2, 3, 4, 5], 7))
print(ob.successfulPairs([15,8,19], [38,36,23], 328))
print(ob.successfulPairs([18], [34,40,20,33,20,38,24,36,35,33], 538))

