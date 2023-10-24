class Solution:
    def postfixEvaluation(self, exp: str):
        stk = []
        operators = ["+", "-", "*", "/", "^"]
        for i in exp:
            if i not in operators:
                stk.append(i)
            else:
                if stk:
                    operand1, operand2 = stk.pop(), stk.pop()
                    stk.append(str(eval(operand2 + i + operand1)))
        return int(stk.pop())


ob = Solution()
print(ob.postfixEvaluation("231*+9-"))
