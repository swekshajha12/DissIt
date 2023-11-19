# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class solution:
    def largest_rectangle(self, arr):
        nsl, nsr = [], []
        stk1, stk2 = [], []
        n = len(arr)
        width = []
        max_area = float('-inf')

        # calculate nearest smaller to the left
        for i in range(n):

            while stk1 and arr[stk1[-1]] >= arr[i]:
                stk1.pop()

            if stk1:
                nsl.append(stk1[-1])
            else:
                nsl.append(-1)
            stk1.append(i)

        # calculate nearest smaller to the right
        for i in range(n - 1, -1, -1):
            while stk2 and arr[stk2[-1]] >= arr[i]:
                stk2.pop()

            if stk2:
                nsr.append(stk2[-1])
            else:
                nsr.append(n)

            stk2.append(i)

        nsr = nsr[::-1]

        for i in range(n):
            width.append(nsr[i] - nsl[i] - 1)
        for i in range(n):
            max_area = max(max_area, arr[i] * width[i])

        return max_area


ob = solution()
print(ob.largest_rectangle([6, 2, 5, 4, 5, 1, 6]))
print(ob.largest_rectangle([2, 1, 5, 6, 2, 3]))
print(ob.largest_rectangle([2, 4]))
