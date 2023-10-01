# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


# We first have to traverse through the given list of characters and store the character and its continuous occurence in a list 'd'.
# Then in the list 'd' created, alter the chars array at any index only if the occurrence is greater than 1.
# Count the number of alters we made and return the count.


class Solution:
    def compress(self, chars: List[str]) -> int:
        dc = []
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                dc.append([chars[i - 1], count])
                count = 1

        dc.append([chars[-1], count])
        i = 0
        for k, v in dc:
            chars[i] = k
            i += 1
            if v > 1:
                for item in str(v):
                    chars[i] = str(item)
                    i += 1
        chars = chars[:i]
        print(chars)
        return i


ob = Solution()
print(ob.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(ob.compress(["a"]))
print(ob.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
