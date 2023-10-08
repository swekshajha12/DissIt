# https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n < 3:
            if n == 0:
                return 0
            else:
                return 1
        else:
            dp[0], dp[1], dp[2] = 0, 1, 1
            for i in range(3, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]


ob = Solution()
print(ob.tribonacci(4))
print(ob.tribonacci(3))
