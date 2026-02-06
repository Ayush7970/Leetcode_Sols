class Solution:

    """
    According to Neetocde, THis is the Dp pattern : Palindrome. In which we start from between while looping through the array
    """
    # def helper(i, j, s):

    #     while i >= 0 and j < len(s) and s[i] == s[j]:
    #         i -= 1
    #         j += 1

    #     return s[i + 1:j]

    # def longestPalindrome(self, s: str) -> str:

    #     if len(s) == 1:
    #         return s

    #     length = 0
    #     max_s = ""
    #     for i in range(len(s) - 1):

    #         output = Solution.helper(i, i, s)
    #         if len(output) > len(max_s):
    #             max_s = output
    #             length = len(output)
        
    #         output = Solution.helper(i, i + 1, s)
    #         if len(output) > len(max_s):
    #             max_s = output
    #             length = len(output)

    #     return max_s


        
        
        















    
    # # sicne this is repitative 

    #     if len(s) == 1:
    #         return s
       
    #     max_s = ""
    #     max_l = 0
    #     rev = ""
    #     for i in range(len(s)):

    #         s1 = s[i]
    #         l1 = 1
    #         if max_l < l1:
    #                 max_s = s1
    #                 max_l = l1
    #         l = i - 1
    #         r = i + 1
            
    #         while l >= 0 and r < len(s) and s[l] == s[r]:

    #             s1 = s[l : r + 1]
    #             l1 = r - l + 1
    #             if max_l < l1:
    #                 max_s = s1
    #                 max_l = l1
    #             l -= 1
    #             r += 1

            

    #         if i + 1 < len(s) and s[i] == s[i + 1]:
    #             l = i 
    #             r = i + 1
    #             s1 = s[l : r + 1]
    #             l1 = r - l + 1
    #             if max_l < l1:
    #                     max_s = s1
    #                     max_l = l1
    #             while l >= 0 and r < len(s) and s[l] == s[r]:

    #                 s1 = s[l : r + 1]
    #                 l1 = r - l + 1
    #                 if max_l < l1:
    #                     max_s = s1
    #                     max_l = l1
    #                 l -= 1
    #                 r += 1

    #     return max_s














    #     # reslen = 0
    #     # res = ""
    #     # for i in range(len(s)):
    #     #     l, r = i, i

    #     #     while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
    #     #         if (r - l + 1) > reslen:
    #     #             reslen = r - l + 1 
    #     #             res = s[l: r + 1]
    #     #         l = l - 1
    #     #         r = r + 1

    #     #     l, r  = i, i + 1
    #     #     while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
    #     #         if (r - l + 1) > reslen:
    #     #             reslen = r - l + 1
    #     #             res = s[l : r + 1]
    #     #         l = l - 1
    #     #         r = r + 1
    #     # return res

















    # # def check(self, s, l, r):

    # #     while l >= 0 and r < len(s) and s[l] == s[r]:
    # #         l -= 1
    # #         r += 1
    # #     return s[l+1:r]
    # # def longestPalindrome(self, s: str) -> str:

    # #     if len(s) <= 1:
    # #         return s

    # #     maxstr = ""
    # #     for i in range(len(s)):
    # #         l = i
    # #         r = i
    # #         odd = Solution.check(self, s, l, r+1)
    # #         even = Solution.check(Self, s, l, r)


    # #         if len(maxstr) < len(even):
    # #             maxstr = even
    # #         if len(maxstr) < len(odd):
    # #             maxstr = odd
            
    # #     return maxstr
        