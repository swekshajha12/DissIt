# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)

        if count1.keys() == count2.keys():
            if sorted(count1.values()) == sorted(count2.values()):
                return True
        return False


ob = Solution()
print(ob.closeStrings('abc', 'bca'))
print(ob.closeStrings('ddabc', 'aabdc'))
