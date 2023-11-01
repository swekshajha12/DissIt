# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75


# To solve this problem we'll use sliding window

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_val, curr_count = 0, 0
        vowel_list = ['a', 'e', 'i', 'o', 'u']

        # first we get the max val in the first k substring
        for i in range(k):
            if s[i] in vowel_list:
                curr_count += 1
        max_val = curr_count

        # then we iterate over the string starting from 1st index
        for i in range(1, len(s)):
            if s[i - 1] in vowel_list:
                curr_count -= 1
            if i + k - 1 < len(s):
                if s[i + k - 1] in vowel_list:
                    curr_count += 1

            if curr_count > max_val:
                max_val = curr_count

        return max_val

    def maxVowelsSl(self, s: str, k: int):
        max_res = 0
        res = 0
        vowels = ["a", "e", "i", "o", "u"]
        for i in range(k):
            if s[i] in vowels:
                res += 1

        for i in range(1, len(s) - k):
            if s[i + k - 1] in vowels:
                res += 1
            if s[i - 1] in vowels:
                res -= 1
            if res > max_res:
                max_res = res
        return max_res


obj = Solution()
print(obj.maxVowels("abciiidef", 3))
print(obj.maxVowels("aeiou", 2))
print(obj.maxVowels("leetcode", 3))
print(obj.maxVowelsSl("abciiidef", 3))
print(obj.maxVowelsSl("aeiou", 2))
print(obj.maxVowelsSl("leetcode", 3))
