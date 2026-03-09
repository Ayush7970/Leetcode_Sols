class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        """
        Bottom Up approach in dp, solving LCS. Make sure you start the dp indexes at i + 1 and j + 1, we always store the value one place ahead for this. Also I changed it -1 everywhere just to learn other approaches.
        """
        
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]


        for i in range(1, len(text1) + 1):

            for j in range(1, len(text2) + 1):

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        print(dp)
        return dp[len(text1)][len(text2)]







        """
        Pattern : DP Longest Common Subsequence (LCS). We soleved this in memoized version in this one. Make sure you always have the condition of checking the length in the base case or any condition to prevent error
        """


        # dp = [[-1] * (len(text2)) for _ in range(len(text1))]
        # def recursive_func(i1, i2):

        #     if i1 >= len(text1) or i2 >= len(text2):
        #         return 0
            
        #     if dp[i1][i2] != -1:
        #         return dp[i1][i2]
            
        #     if text1[i1] == text2[i2]:
        #         dp[i1][i2] =  1 + recursive_func(i1 + 1, i2 + 1)
        #     else:
        #         dp[i1][i2] = max(recursive_func(i1 + 1, i2), recursive_func(i1, i2 + 1))
            
        #     return dp[i1][i2]

        # return recursive_func(0, 0)

        
 
        













        # dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        # for i in range(len(text1) -1, -1, -1):
        #     for j in range(len(text2) - 1, -1, -1):

        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        # return dp[0][0]


        # dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        # for i in range(len(text1)-1, -1, -1):

        #     for j in range(len(text2)-1, -1, -1):

        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # return dp[0][0]        