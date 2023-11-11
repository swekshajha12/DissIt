# https://leetcode.com/problems/partition-equal-subset-sum/description/

class Solution:

    def recursive_sol_wrong(self, arr, s1, s2, n):
        if n == 0 and s1 == s2:
            return True
        if n == 0 and s1 != s2:
            return False
        if s1 < s2 or s1 == 0:
            return self.recursive_sol(arr, s1 + arr[n - 1], s2, n - 1) or self.recursive_sol(arr, s1, s2, n - 1)
        else:
            return self.recursive_sol(arr, s1, s2 + arr[n - 1], n - 1) or self.recursive_sol(arr, s1, s2, n - 1)

    def recursive_sol(self, arr):

        def sol_impl(arr, target, n):
            if n == 0 and target != 0:
                return False
            if target == 0:
                return True
            if arr[n - 1] <= target:
                return sol_impl(arr, target - arr[n - 1], n - 1) or sol_impl(arr, target, n - 1)
            else:
                return sol_impl(arr, target, n - 1)

        if sum(arr) % 2 != 0:
            return False
        else:
            return sol_impl(arr, sum(arr) // 2, len(arr))


ob = Solution()
print(ob.recursive_sol([1, 5, 11, 5]))
