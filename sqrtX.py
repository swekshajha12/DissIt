# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        ans = 1
        for i in range(x):
            if i * i <= x:
                ans = i
            else:
                break
        return ans


ob = Solution()
print(ob.mySqrt(32))
