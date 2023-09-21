# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack, len_needle = len(haystack), len(needle)
        for i in range(len_haystack):
            if haystack[i]==needle[0] and i+len_needle<=len_haystack:
                temp = haystack[i:i+len_needle]
                if temp == needle:
                    return i
        return -1

ob = Solution()
print(ob.strStr("sadbutsad", "sad"))
print(ob.strStr("sadbutsad", "a"))
print(ob.strStr("a", "a"))