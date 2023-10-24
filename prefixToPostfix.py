class Solution:
    def infixToPostfix(self, exp: str):
        res = ""
        stk = []
        precedence_map = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

        for i in exp:
            if i.isdigit() or i.isalpha():
                res += i
            else:
                if not stk:
                    stk.append(i)
                else:
                    if precedence_map[stk[-1]] >= precedence_map[i]:
                        while stk and precedence_map[stk[-1]] >= precedence_map[i]:
                            res += stk.pop()
                    stk.append(i)

        if stk:
            while stk:
                res += stk.pop()

        return res


ob = Solution()
print(ob.infixToPostfix("a+b*c+d"))
