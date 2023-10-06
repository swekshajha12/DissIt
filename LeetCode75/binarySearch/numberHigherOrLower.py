# https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

def guess(num: int) -> int:
    res = 6
    if num > res:
        return -1
    elif num < res:
        return 1
    elif num == res:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        mid = n // 2
        left = 1
        right = n

        if n == 1:
            return n

        while left < right:
            if guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == 0:
                return mid
            mid = (left + right) // 2

        return mid


ob = Solution()
print(ob.guessNumber(10))
