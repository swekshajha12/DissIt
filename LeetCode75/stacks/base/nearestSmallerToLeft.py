class Solution:
    def search(self, arr):
        n = len(arr)
        stk, res = [], []
        for i in range(n):
            while stk and stk[-1] >= arr[i]:
                stk.pop()

            if stk:
                res.append(stk[-1])
            else:
                res.append(-1)
            stk.append(arr[i])

        return res


ob = Solution()
print(ob.search([4, 5, 2, 10, 8]))
print(ob.search([1, 1, 1, 1, 1]))
