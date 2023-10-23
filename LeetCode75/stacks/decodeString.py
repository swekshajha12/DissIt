# https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for char in s:
            if char != "]":
                stk.append(char)
            else:
                temp_str = ""
                while stk[-1] != "[":
                    stk_top = stk.pop()
                    temp_str = stk_top + temp_str

                stk.pop()

                digit = ""
                while stk and stk[-1].isdigit():
                    stk_top = stk.pop()
                    digit = stk_top + digit

                stk.append(int(digit) * temp_str)

        return "".join(stk)


obj = Solution()
print(obj.decodeString("30[a]2[bc]"))
print(obj.decodeString("3[a2[bc]]"))
# print(obj.decodeString("2[abc]3[cd]ef"))
print(obj.decodeString("100[leetcode]"))
