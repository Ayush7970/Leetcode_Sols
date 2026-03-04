class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        """
        Simple easy question. You loop through an both string. If both match you move both forward else you move the main string. You handle the edge case as well. 
        """

        if not s or not t:
            return not s


        i, j = 0, 0

        while i < len(s) and j < len(t):
            print(i, j)

            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return True if i == len(s) else False
        
        