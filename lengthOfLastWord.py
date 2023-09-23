# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words_list = s.split(" ")[::-1]
        for word in words_list:
            if word != "":
                return len(word)
        return 0

