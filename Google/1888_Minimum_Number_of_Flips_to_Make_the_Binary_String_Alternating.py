class Solution:
    def minFlips(self, s: str) -> int:
        """
        Try Again
        Amazing question: Type Dynamic programming Sliding Window with a trick.
        The question was counting type 2 change but typ1 change is free to apply. The tricky part of this question was that 1) You cna apply type 1 which can be perfectly handled in o(1) if you just add the same string again and use sliding window. 2) For checking the minimum changes you just need to count the differences, and when you shift to the next letter through sliding window, you just need to calculate the next character not the repeated work, since it will remain same as we are taking alt1 and alt2 twice as well. 
        T.C -> O(n)
        S.C -> O(n)
        """
        n = len(s)
        s += s
        alt1, alt2 = "", ""

        for i in range(len(s)):
            alt1 += "1" if i % 2 == 0 else "0"
            alt2 += "0" if i % 2 == 0 else "1"

        l = 0
        diff1, diff2 = 0, 0
        res = n
        for r in range(len(s)):

            if alt1[r] != s[r]:
                diff1 += 1
            if alt2[r] != s[r]:
                diff2 += 1
            
            if r - l + 1 > n:
                if alt1[l] != s[l]:
                    diff1 -= 1
                if alt2[l] != s[l]:
                    diff2 -= 1
                l += 1
            
            if r - l + 1 == n:
                res = min(res, diff1, diff2)
        
        return res


        