class Solution:
    def lcsubstring_rec(self, s1, s2, m, n):

        def solve(s1, s2, m, n, res):
            if m == 0 or n == 0:
                return res

            if s1[m - 1] == s2[n - 1]:
                return solve(s1, s2, m - 1, n - 1, res + 1)
            else:
                return max(res, max(solve(s1, s2, m, n - 1, 0), solve(s1, s2, m - 1, n, 0)))

        return solve(s1, s2, m, n, 0)

    def lcssubstring_tab(self, s1, s2, m, n):
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[j - 1] == s2[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0

        max_res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                max_res = max(max_res, dp[i][j])

        return max_res

    # https: // leetcode.com / problems / maximum - length - of - repeated - subarray / description /
    def subArray(self, arr1, arr2):
        m, n = len(arr1), len(arr2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if arr1[i - 1] == arr2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0

        max_res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                max_res = max(max_res, dp[i][j])

        return max_res


ob = Solution()
print(ob.lcsubstring_rec("abcdef", "abzcde", 6, 6))
print(ob.lcssubstring_tab("abcdef", "abzcde", 6, 6))
print(ob.subArray([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
