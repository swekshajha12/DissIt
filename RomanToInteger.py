
# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        out,s_old,s_curr=0,0,0
        roman_int_map = {"I":1, "V":5, "X":10, "L":50, "C":100,
        "D":500, "M":1000}
        len_s=len(s)
        for i in range(len_s):
            s_curr = roman_int_map[s[i]]
            if s_old ==0:
                s_old = s_curr
                continue
            elif s_old >=s_curr:
                out+=s_old
            elif s_old < s_curr:
                s_curr = s_curr-s_old
            s_old = s_curr
        out+=s_curr
        return out
        
