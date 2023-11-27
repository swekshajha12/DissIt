# https://leetcode.com/problems/maximal-rectangle/description/
from typing import List


class Solution:
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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        arr =[]
        max_area = float('-inf')
        rows, cols = len(matrix), len(matrix[0])
        for j in range(cols):
            arr.append(int(matrix[0][j]))
        max_area = max(max_area, self.largest_rectangle(arr))

        for i in range(1, rows):
            for j in range(cols):
                print(i, j , matrix[i][j])
                if matrix[i][j]=="0":
                    arr[j]=0
                else:
                    arr[j]=arr[j]+int(matrix[i][j])
            max_area = max(max_area, self.largest_rectangle(arr))

        return max_area


ob = Solution()
print(ob.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(ob.maximalRectangle([["0"]]))
print(ob.maximalRectangle([["1"]]))
print(ob.maximalRectangle([["0","1"],["1","0"]]))


