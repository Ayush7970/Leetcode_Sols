class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        This question was easy it was the part of adding and multiplication numbers in strings series, The tricky part was filling up the zero, there can be a bit. manupilation solution.

        T.C -> O(max(a, b))
        S.C -> (O(max(a, b)))
        """


        n = max(len(a), len(b))
        ans = []
        a, b = a.zfill(n), b.zfill(n)                   # that was the tricky part, i though of it but there is an inbuilt function for filling zeros to strings
        carry = 0
        for i in range(n - 1, -1, -1):

            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1
            
            if carry % 2 == 1:
                ans.append(1)
            else:
                ans.append(0)
            
            carry //= 2
        
        if carry % 2 == 1:
            ans.append(1)
        return "".join(str(val) for val in reversed(ans))

            


        



        

        