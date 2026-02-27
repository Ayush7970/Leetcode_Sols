class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        """
        Simple stack question, generally aritimatic equation questions are mostly stack use, remember this.
        """
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] in "+-*/":
                val1 = stack.pop()
                val2 = stack.pop()
                if tokens[i] == "+":
                    res = int(val1) + int(val2)
                elif tokens[i] == "-":
                    res = int(val2) - int(val1)
                elif tokens[i] == "*":
                    res = int(val1) * int(val2)
                elif tokens[i] == "/":
                    res = int(val2) / int(val1)
                stack.append(res)

            else:
                stack.append(tokens[i])
            
            i += 1
        
        return int(stack[0])










    

    #     stack = []

    #     for t in tokens:

    #         if t == '+':
    #             stack.append(stack.pop() + stack.pop())
    #         elif t == '-':
    #             a, b = stack.pop(), stack.pop()
    #             stack.append(int(b - a))
    #         elif t == '*':
    #             stack.append(stack.pop() * stack.pop())
    #         elif t == '/':
    #             a, b = stack.pop(), stack.pop()
    #             stack.append(int(b / a))
    #         else:
    #             stack.append(int(t))
    #     return stack.pop()
        


        
        