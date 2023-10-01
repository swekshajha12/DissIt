# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75


# To solve this question, we'll use stack


class Solution:
    def reverseVowels(self, s: str) -> str:
        pos, vowels = [], []
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(s)):
            if s[i] in vowel_list:
                pos.append(i)
                vowels.append(s[i])
        res_str = list(s)
        for i in pos:
            if vowels:
                x = vowels.pop()
                res_str[i] = x
        return ''.join(res_str)


ob = Solution()
res = ob.reverseVowels("hello")
print(res)
