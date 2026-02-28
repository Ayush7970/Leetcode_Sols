from ast import List

class Solution:

    """
    Try it again.
    A bit tough question. It was about solving the mathemiactical equations issue of left o right and bracket precedence. Morever, I made the wrong choice and started with recursion. Although it is possible withv recursion. It is much more feasible with stack. Always remember to solve () or equation precendence stack are most useful.

    For this question we ahve to follow the left to right preference in the main equation, so we reverse loop the equation from the back. Therefore, ( becomes ) and ) becomnes (
    """
    def evaluate(stack):
        print(type(stack[-1]))
        if not stack or type(stack[-1]) == str:
            stack.append(0)
        
        res = stack.pop()


        while stack and stack[-1] != ")":
            sign = stack.pop()
            if sign == "+":
                res += stack.pop()
            else:
                res -= stack.pop()
        return res


    def calculate(self, s: str) -> int:

        n = 0
        operand = 0
        stack = []
        for i in range(len(s) -1, -1, -1):
            ch = s[i]
            if ch.isdigit():

                operand = (int(ch) * (10 ** n)) + operand
                n += 1
            
            elif ch != " ":
                if n:
                
                    stack.append(operand)
                    n = 0
                    operand = 0

                if ch == "(":
                    res = Solution.evaluate(stack)

                    stack.pop()

                    stack.append(res)

                else:
                    stack.append(ch)
        
        if n: 
            stack.append(operand)
        
        return Solution.evaluate(stack)
        