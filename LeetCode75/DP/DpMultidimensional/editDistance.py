# https://leetcode.com/problems/edit-distance/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf')] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        dp[0][0] = 0
        # populate base case for first row i.e empty string
        for j in range(1, len(word1) + 1):
            dp[0][j] = j

        # populate base case for first column i.e empty string
        for i in range(1, len(word2) + 1):
            dp[i][0] = i

        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                # doing i-1, j-1 because word indexing would be starting from 0
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[len(word2)][len(word1)]


ob = Solution()
print(ob.minDistance("horse", "ros"))
print(ob.minDistance("intention", "execution"))
