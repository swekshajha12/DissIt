# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if count == n:
                return True
            if i == 0 and len(flowerbed) == 1 and n == 1 and flowerbed[i] == 0:
                flowerbed[i] = 1
                count += 1
            elif i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
            elif i != len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1

            elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                count += 1

        return count == n

    def canPlaceFlowersSimplified(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            # Check if we can plant a flower at the current position (i)
            if (
                    flowerbed[i] == 0  # Current position is empty
                    and (i == 0 or flowerbed[i - 1] == 0)  # Previous position is empty (or it's the first position)
                    and (i == length - 1 or flowerbed[i + 1] == 0)  # Next position is empty (or it's the last position)
            ):
                flowerbed[i] = 1  # Plant a flower at the current position
                count += 1  # Increment the count of planted flowers

            if count >= n:
                return True  # We have planted enough flowers

        return count >= n


ob = Solution()
# print(ob.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
# print(ob.canPlaceFlowers([0],1))
print(ob.canPlaceFlowers([0, 0, 1, 0, 0], 1))
