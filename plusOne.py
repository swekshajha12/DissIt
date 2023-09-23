# https://leetcode.com/problems/plus-one/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        orginal_num = ''.join(str(i) for i in digits)
        updated_num = int(orginal_num)+1
        for num in str(updated_num):
            res.append(int(num))
        return res

ob = Solution()
print(ob.plusOne([1,2,3]))
