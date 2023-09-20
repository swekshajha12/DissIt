# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        dc = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in list(dc.values()):
                stk.append(i)
            if i in list(dc.keys()):
                if not stk:
                    return False
                x = stk.pop()
                if x != dc[i]:
                    return False
        if not stk:
            return True
        return False

