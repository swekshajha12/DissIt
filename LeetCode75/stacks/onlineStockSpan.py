# https://leetcode.com/problems/online-stock-span/description/

class Solution:
    def span(self, arr):
        res, stk = [], []
        n = len(arr)
        for i in range(n):
            while stk and arr[stk[-1]]<=arr[i]:
                stk.pop()

            if stk:
                res.append(i-stk[-1])
            else:
                res.append(i+1)

            stk.append(i)

        return res

ob = Solution()
print(ob.span([80, 80, 60, 70,60,75,85]))