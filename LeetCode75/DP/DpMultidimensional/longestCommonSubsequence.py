# https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=leetcode-75


# You can't use dfs for this question as the maximum subsequence can occur in any order
# class Solution1:
#
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         count = 0
#         m, n = len(text1), len(text2)
#         visited = [[0] * (m + 1) for _ in range(n + 1)]
#         print(len(visited), len(visited[0]))
#
#         if m == n and m == 1 and text1 == text2:
#             return 1
#
#         def markVisited(visited, i, j, m, n):
#             if i < 0 or i >= n + 1 or j < 0 or j >= m + 1 or visited[i][j] == 1:
#                 return
#
#             visited[i][j] = 1
#             markVisited(visited, i + 1, j, m, n)
#             markVisited(visited, i - 1, j, m, n)
#             markVisited(visited, i, j - 1, m, n)
#
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 if text2[i - 1] == text1[j - 1]:
#                     print(text2[i-1], text1[j-1])
#                     if visited[i][j] != 1:
#                         print(visited[i][j])
#                         markVisited(visited, i, j, m, n)
#                         print(visited)
#                         count += 1
#         return count


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * n + 1 for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


ob = Solution()
print(ob.longestCommonSubsequence("abcde", "ace"))
print(ob.longestCommonSubsequence("abc", "abc"))
print(ob.longestCommonSubsequence("abc", "def"))
print(ob.longestCommonSubsequence("ezupkr", "ubmrapg"))
print(ob.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))
