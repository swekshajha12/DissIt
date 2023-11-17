# https://www.codingninjas.com/studio/problems/ceiling-in-a-sorted-array_1825401

class Solution:
    def getFloor(self, arr, n, x):
        left, right = 0, n - 1
        min_res = float('-inf')
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                return arr[mid]
            elif arr[mid] < x:
                min_res = max(min_res, arr[mid])
                left = mid + 1
            else:
                right = mid - 1
        if min_res == float('-inf'):
            return -1
        return min_res

    def getCeil(self, arr, n, x):
        left, right = 0, n - 1
        res = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                return arr[mid]
            if arr[mid] > x:
                res = min(res, arr[mid])
                right = mid - 1
            else:
                left = mid + 1

        if res == float('inf'):
            return -1
        return res

    def getFloorAndCeil(self, a, n, x):
        floor, ceil = self.getFloor(a, n, x), self.getCeil(a, n, x)
        return floor, ceil


ob = Solution()
print(ob.getFloorAndCeil([6, 6, 7, 12, 16, 18, 19, 22, 23, 30], 10, 14))
