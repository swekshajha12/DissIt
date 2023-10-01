# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def gcdOfStrings(self, str1, str2):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        len1, len2 = len(str1), len(str2)
        common_length = gcd(len1, len2)
        if str1 + str2 != str2 + str1:
            return ""
        else:
            return str1[:common_length]


# Example usage:
str1 = "ABABAB"
str2 = "ABA"
ob = Solution()
result = ob.gcdOfStrings(str1, str2)
print(result)  # Output: "ABC"
