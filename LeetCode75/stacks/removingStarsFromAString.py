# https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for char in s:
            if char != "*":
                stk.append(char)
            else:
                if stk:
                    stk.pop()

        return "".join(stk)



obj = Solution()
print(obj.removeStars("leet**cod*e"))
print(obj.removeStars("erase*****"))
