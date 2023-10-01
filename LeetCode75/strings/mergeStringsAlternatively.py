# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

# we'll use stack for this problem

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        stk1 = list(word1[::-1])
        stk2 = list(word2[::-1])
        res = ""
        while stk1 and stk2:
            res += stk1.pop() + stk2.pop()

        if stk1:
            while stk1:
                res += stk1.pop()

        if stk2:
            while stk2:
                res += stk2.pop()

        return res


ob = Solution()
res = ob.mergeAlternately("Hello", "How")
print(res)
