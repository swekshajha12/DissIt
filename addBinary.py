# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        answer = []
        carry = 0
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')

            carry //= 2
        if carry == 1:
            answer.append('1')
        answer.reverse()
        return ''.join(answer)

ob = Solution()
print(ob.addBinary("11", "1"))

