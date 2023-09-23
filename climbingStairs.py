# https://leetcode.com/problems/climbing-stairs/description/

# it's fibonacci in disguise
class Solution:
    def climbStairsRecursive(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # non recursive solution
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            while n - 2:
                c = a + b
                a = b
                b = c
                n -= 1
            return c


ob = Solution()
print(ob.climbStairs(5))
