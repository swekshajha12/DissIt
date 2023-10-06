# https://leetcode.com/problems/daily-temperatures/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                j = stk.pop()
                ans[j] = i - j
            stk.append(i)

        return ans


ob = Solution()
print(ob.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
