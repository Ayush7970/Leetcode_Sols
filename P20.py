class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        for i in s:

            if i == ")":
                if stack and stack.pop() == "(":
                    continue
                else:
                    return False
            if i == "}":
                if stack and stack.pop() == "{":
                    continue
                else:
                    return False

            if i == "]":
                if stack and stack.pop() == "[":
                    continue
                else:
                    return False
            else:
                stack.append(i)


        return True if not stack else False




















        # stack = []
        # for i in range(len(s)):

        #     if s[i] == "(" or s[i] == "{" or s[i] == "[":
        #         stack.append(s[i])
        #     else:
        #         if len(stack) == 0:
        #             return False
        #         ch = stack[-1]
        #         if (s[i] == ")" and ch == "(") or (s[i] == "}" and ch == "{") or (s[i] == "]" and ch == "["):
        #             stack.pop()
        #         else:
        #             return False
        # if len(stack) != 0:
        #     return False
        # return True



        