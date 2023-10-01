# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

# we'll use 2 pointer approach here

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if t[p2] == s[p1]:
                count += 1
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        if count == len(s):
            return True
        else:
            return False


ob = Solution()
print(ob.isSubsequence("abc", "ahbgdc"))
print(ob.isSubsequence("axc", "ahbgdc"))
print(ob.isSubsequence("", ""))
