class Solution:


    """
    Dp pattern: Palindrome, In this you expand from the middle.
    """

    # def helper(i, j, s):

    #     count = 0
    #     while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
    #         i -= 1
    #         j += 1
    #         # print(s[i + 1: j])
    #         count += 1
    #     return count
    
    # def countSubstrings(self, s: str) -> int:

    #     count = 0
    #     for i in range(len(s)):

    #         count += Solution.helper(i, i, s)
    #         count += Solution.helper(i, i + 1, s)
        
    #     return count



        


