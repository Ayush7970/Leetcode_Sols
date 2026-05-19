class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        """
        T.C -> O(n) worst case
        Simple easy question, loop from back and when any space apper after any letter, just break.
        """

        count = 0
        cond = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                count += 1
                cond = True
            elif cond:
                break
        return count
                

