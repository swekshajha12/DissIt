# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        len_x = len(x_str)
        low, high = 0, len_x - 1
        if len_x == 0:
            return False
        else:
            while (low < high):
                if (x_str[low] == x_str[high]):
                    low += 1
                    high -= 1
                    continue
                else:
                    return False
            return True
