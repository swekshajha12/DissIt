# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common_pre = ""
        min_str, min_size = "", 201
        for i in strs:
            if len(i) < min_size:
                min_size = len(i)
                min_str = i
        stk = list(min_str)[::-1]
        if len(stk) == 0:
            return ""
        for string in strs:
            common_pre = ""
            if string[0] != stk[-1]:
                return common_pre
            for i in string:
                if len(stk) != 0:
                    print(i)
                    print(stk)
                    if i == stk[-1]:
                        common_pre += i
                        stk.pop()
                    else:
                        break

            stk = list(common_pre)[::-1]
        return common_pre

#optimised sol
# class Solution:
#     def longestCommonPrefix(self, v: List[str]) -> str:
#         ans=""
#         v=sorted(v)
#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans