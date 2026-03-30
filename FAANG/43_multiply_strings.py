class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        """
        Also remember whenever you multiply any number its length of digits will always be (m + n) or (m + n - 1)
        Great String and Math question. A bit confusing.
        You have to do it the elementary way. You must take care of the carry value and values of the zeros. Therefore we reversed the strings and used position and ans array. At the end we reversed the result as well.
        T.C -> O(len(num1) * len(num2))
        S.C -> O(len(num1) + len(num2))
        """
        if num1 == "0" or num2 == "0":
            return "0"


        num1 = num1[::-1]
        num2 = num2[::-1]

        ans = [0] * (len(num1) + len(num2))
        for p1, v1 in enumerate(num1):


            for p2, v2 in enumerate(num2):

                position = p1 + p2

                carry = ans[position]

                multiplication = int(v1) * int(v2) + carry

                ans[position] = multiplication % 10

                ans[position + 1] += multiplication // 10

        if ans[-1] == 0:
            ans.pop()
        
        return "".join(str(digit) for digit in reversed(ans))

















        









        # if "0" in [num1, num2]:
        #     return 0
        
        # num1 = num1[::-1]
        # num2 = num2[::-1]
        # res = [0] * (len(num1) + len(num2))
        # for i in range(len(num1)):
        #     for j in range(len(num2)):
        #         digit = int(num1[i]) * int(num2[j])
        #         res[i + j] += digit
        #         res[i + j + 1] += res[i + j] // 10
        #         res[i + j] = res[i + j] % 10

        # res = res[::-1]
        # index = 0
        # while index < len(res) and res[index] == 0:
        #     index += 1
        # res = map(str, res[index:])
        # return "".join(res)
                

        
        