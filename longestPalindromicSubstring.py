# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_len = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_len = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
        return res

    def checkPalindrome(self, s):
        n = len(s)
        l, r = 0, n - 1

        while (l < r):
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        return True

    def longestPalindromicSubstringBruteForce(self, s: str):
        n = len(s)
        res = []
        substrs = []
        for i in range(n):
            substrs.append(s[0:i + 1])

        for substr in substrs:
            isPalin = self.checkPalindrome(substr)
            if isPalin:
                res.append(len(substr))
            else:
                res.append(1)
        print(res)
        return max(res)


# expand approach
ob = Solution()
print(ob.longestPalindrome("babad"))
print(ob.longestPalindrome("ac"))
print(ob.longestPalindrome("abb"))
print(ob.longestPalindromicSubstringBruteForce("babad"))

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         dp = [[False for i in range(len(s))] for i in range(len(s))]
#         for i in range(len(s)):
#             dp[i][i] = True
#         max_length = 1
#         start = 0
#         for l in range(2, len(s) + 1):
#             for i in range(len(s) - l + 1):
#                 end = i + l
#                 if l == 2:
#                     if s[i] == s[end - 1]:
#                         dp[i][end - 1] = True
#                         max_length = l
#                         start = i
#                 else:
#                     if s[i] == s[end - 1] and dp[i + 1][end - 2]:
#                         dp[i][end - 1] = True
#                         max_length = l
#                         start = i
#         return s[start:start + max_length]

# ob = Solution()
# print(ob.longestPalindrome("babad"))
# print(ob.longestPalindrome("ac"))
# print(ob.longestPalindrome("abb"))
