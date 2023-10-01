# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75
from re import sub


class Solution:
    def reverseWords(self, s: str) -> str:
        if s == " ":
            return ""
        temp = ""
        res = ""
        s = s.lstrip(" ")
        s = s.rstrip(" ")
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                temp += s[i]
            else:
                if s[i - 1] != " ":
                    res += temp[::-1] + " "
                else:
                    res += temp[::-1]
                temp = ""
        res += temp[::-1]
        return res

    def reverseWordsOneLiner(self, s: str) -> str:
        return ' '.join(sub(r'\s{1,}', ' ', s.strip()).split(' ')[::-1])


ob = Solution()
# print(ob.reverseWords("  hello world  "))
print(ob.reverseWords("a good   example"))
print(ob.reverseWordsOneLiner("a good   example"))
