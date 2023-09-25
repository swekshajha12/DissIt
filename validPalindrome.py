# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNumStr = ""
        for i in s.lower():
            if i.isdigit() or i.isalpha():
                alphaNumStr += i

        if len(alphaNumStr) == 0:
            return True

        low, high = 0, len(alphaNumStr) - 1
        while low < high:
            if alphaNumStr[low] != alphaNumStr[high]:
                return False
            low += 1
            high -= 1
        return True


ob = Solution()
print(ob.isPalindrome("A man, a plan, a canal: Panama"))
print(ob.isPalindrome("race a car"))
print(ob.isPalindrome("0P"))
