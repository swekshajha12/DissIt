# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/

# Todo: on hold for negative scenarios

class Solution:
    def recursive(self, arr):
        min_res = float('inf')

        def solve(arr, target, n):
            if n <= 0 and target != 0:
                return False
            if target == 0:
                return True
            if arr[n - 1] <= target:
                return solve(arr, target - arr[n - 1], n - 1)
            else:
                return solve(arr, target, n - 1)

        k_range = sum(arr)
        if k_range == 0:
            pos_sum = 0
            neg_sum = 0
            for i in range(len(arr)):
                if arr[i] < 0:
                    neg_sum += arr[i]
                if arr[i] >= 0:
                    pos_sum += arr[i]
            return pos_sum - neg_sum
        if k_range > 0:
            for i in range((k_range // 2) + 1):
                isPossible = solve(arr, i, len(arr))
                if isPossible:
                    min_res = min(min_res, k_range - (2 * i))
        else:
            for i in range(k_range, 1):
                isPossible = solve(arr, i, len(arr))
                if isPossible:
                    min_res = min(min_res, (2 * i)-k_range)
        return min_res


ob = Solution()
print(ob.recursive([1, 2, 7]))
print(ob.recursive([3, 9, 7, 3]))
print(ob.recursive([-36, 36]))
print(ob.recursive([2, -1, 0, 4, -2, -9]))
