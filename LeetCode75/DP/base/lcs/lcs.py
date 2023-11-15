# https://leetcode.com/problems/longest-common-subsequence/description/

class Solution:
    def lcs_recursive(self, s1, s2, n, m):
        if n == 0 or m == 0:
            return 0
        if s1[n - 1] == s2[m - 1]:
            return 1 + self.lcs_recursive(s1, s2, n - 1, m - 1)
        else:
            return max(self.lcs_recursive(s1, s2, n, m - 1), self.lcs_recursive(s1, s2, n - 1, m))

    def lcs_recursive_memoization(self, s1, s2, n, m):
        self.dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        def solve(s1, s2, n, m):
            if n == 0 or m == 0:
                return 0
            if self.dp[n][m] != -1:
                return self.dp[n][m]
            if s1[n - 1] == s2[m - 1]:
                self.dp[n][m] = 1 + solve(s1, s2, n - 1, m - 1)
            else:
                self.dp[n][m] = max(solve(s1, s2, n, m - 1),
                                    solve(s1, s2, n - 1, m))
            return self.dp[n][m]

        return solve(s1, s2, n, m)

    def lcs_tab(self, s1, s2, n, m):
        dp_tab = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp_tab[i][j] = 1 + dp_tab[i - 1][j - 1]
                else:
                    dp_tab[i][j] = max(dp_tab[i][j - 1], dp_tab[i - 1][j])
        # print(dp_tab)
        return dp_tab[n][m]


ob = Solution()
print(ob.lcs_recursive("abcde", "ace", 5, 3))
print(ob.lcs_recursive("abc", "abc", 3, 3))
print(ob.lcs_recursive("abc", "def", 3, 3))
print(ob.lcs_recursive("ezupkr", "ubmrapg", 6, 7))
print(ob.lcs_recursive("oxcpqrsvwf", "shmtulqrypy", len("oxcpqrsvwf"), len("shmtulqrypy")))

print(ob.lcs_recursive_memoization("abcde", "ace", 5, 3))
print(ob.lcs_recursive_memoization("abc", "abc", 3, 3))
print(ob.lcs_recursive_memoization("abc", "def", 3, 3))
print(ob.lcs_recursive_memoization("ezupkr", "ubmrapg", 6, 7))
print(ob.lcs_recursive_memoization("oxcpqrsvwf", "shmtulqrypy", len("oxcpqrsvwf"), len("shmtulqrypy")))

print(ob.lcs_tab("abcde", "ace", 5, 3))
print(ob.lcs_tab("abc", "abc", 3, 3))
print(ob.lcs_tab("abc", "def", 3, 3))
print(ob.lcs_tab("ezupkr", "ubmrapg", 6, 7))
print(ob.lcs_tab("oxcpqrsvwf", "shmtulqrypy", len("oxcpqrsvwf"), len("shmtulqrypy")))
