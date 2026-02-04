class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        """
        Dp LCS pattern, solved with Bootm up approach. ALways make sure you reate the table for bottom up approah. It is really easy for LCS dynamic programming and it is all pattern.
        """

        dp = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][0] = i
        
        for i in range(len (word2) + 1):
            dp[0][i] = i

        print(dp)
        dp[0][0] = 0 
        for i in range(1, len(word1) + 1):

            for j in range(1, len(word2) + 1):

                if word1[i - 1] == word2[j - 1]:

                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        
        return dp[len(word1)][len(word2)]
            







        """
        Dp LCS by memoized approach. Remember when you reached the end of one string you have to find out the differnce between the j adn the end of the other string. You always do the mistake of doing i - j
        """

        # dp = [[-1] * (len(word2) + 1) for _ in range(len(word1))]

        # def dfs(i , j):
        #     if i == len(word1):
        #         return len(word2) - j    ####### YOU MADE THIS MISTAKE TWICE  
        #     if j == len(word2):
        #         return len(word1) - i
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     if word1[i] == word2[j]:

        #         dp[i][j] = dfs(i + 1, j + 1)
        #     else:
        #         dp[i][j] = 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))
            
        #     return dp[i][j]

        # return dfs(0, 0)




















        
        # dp = {}

        # def dfs(i, j):

        #     if i == len(word1):
        #         return len(word2) - j
        #     if j == len(word2):
        #         return len(word1) - i
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     if word1[i] == word2[j]:
        #         dp[(i, j)] = dfs(i + 1, j + 1)
        #     else:
        #         res = min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
        #         dp[(i, j)] = res + 1
        #     return dp[(i, j)]
        
        # return dfs(0, 0)
            


            
            





















        # dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # for i in range(len(word1) + 1):
        #     dp[i][len(word2)] = len(word1) - i
        
        # for j in range(len(word2) + 1):
        #     dp[len(word1)][j] = len(word2) - j


        # for i in range(len(word1) - 1, -1, -1):
        #     for j in range(len(word2) - 1, -1, -1):

        #         if word1[i] == word2[j]:
        #             dp[i][j] = dp[i+1][j+1]
        #         else:
        #             dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
        # return dp[0][0]

    