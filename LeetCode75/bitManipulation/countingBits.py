# https://leetcode.com/problems/counting-bits/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def decimalToBinary(self, num):
        binary = ""
        count = 0
        while num > 0:
            remainder = num % 2
            if remainder == 1:
                count += 1
            binary = str(remainder) + binary
            num = num // 2

        return count

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(self.decimalToBinary(i))
        return res

    def countBitsOptimised(self, n):
        if n == 0:
            return [0]

        # dp array and base cases
        dp_array = [0 for x in range(n + 1)]
        dp_array[1] = 1

        # iterate over the dp array
        for x in range(2, n + 1):

            # if a number is even, check the index in the
            # dp array at index x//2, if uneven do the same but add one
            if x % 2 == 0:
                dp_array[x] = dp_array[x // 2]
            else:
                dp_array[x] = dp_array[x // 2] + 1

        return dp_array


ob = Solution()
print(ob.countBits(2))
print(ob.countBits(5))
print(ob.countBitsOptimised(2))
print(ob.countBitsOptimised(5))
