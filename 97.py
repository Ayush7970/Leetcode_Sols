class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        """
        Following LCS pattern with bottom up approach in DP. 
        """

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):

                k = i + j - 1
                from_s1 = dp[i - 1][j] and s1[i - 1] == s3[k]
                from_s2 = dp[i][j - 1] and s2[j - 1] == s3[k]
                dp[i][j] = from_s1 or from_s2

        return dp[len(s1)][len(s2)]
       

        """
        LCS dp patterrn solved with memoization
        """

        # if len(s1) + len(s2) != len(s3):
        #     return False

        # dp = {}

        # def dfs(i, j, k):
            
        #     if i + j == len(s3):
        #         return True

        #     if (i, j) in dp:
        #         return dp[(i, j)]
                
        #     output = output2 = False
        #     if i < len(s1) and s1[i] == s3[k]:
        #         output = dfs(i + 1, j, k + 1)
        #     if j < len(s2) and s2[j] == s3[k]:
        #         output2 = dfs(i, j + 1, k + 1)
            
        #     dp[(i, j)] = output or output2
        #     return dp[(i, j)]

        # return dfs(0, 0, 0)


















        # dp = {}
        

        # def dfs(i, j):
        #     if  (i + j) == len(s3):
        #         return i == len(s1) and j == len(s2)
        #     if (i, j) in dp:
        #         return dp[(i, j)]
            
        #     if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
        #         return True
        #     if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
        #         return True
        #     dp[(i, j)] = False
        #     return False


        # return dfs(0, 0)





        # if len(s1) + len(s2) != len(s3):
        #     return False
        
        # dp = [[False for i in range(len(s2) + 1)]  for j in range(len(s1) + 1)]
        # dp[len(s1)][len(s2)] = True

        # for i in range(len(s1), -1 ,-1):
        #     for j in range(len(s2), -1, -1):

        #         if i < len(s1) and s1[i] == s3[i+j] and dp[i +1][j]:
        #             dp[i][j] = True
        #         if j < len(s2) and s2[j] == s3[i + j] and dp[i][j+1]:
        #             dp[i][j] = True
        # return dp[0][0] 
        