class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        """
        dp LCS Pattern Bottom up Approach. Understands properly how which cell is getting checked and which cell is getting filled. This is Important. 
        """


        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        dp[0][0] = 1

        for i in range(len(s) + 1):
            dp[i][0] = 1

        for i in range(1, len(s) + 1):

            for j in range(1, len(t) + 1):

                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(s)][len(t)]



        # dp = {}
        # def dfs(i, j):
        #     if j == len(t):
        #         return 1

        #     if i == len(s) :
        #         return 0

        #     if (i, j) in dp:
        #         return dp[(i, j)]
            
        #     if s[i] == t[j]:
        #         dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
        #     else:
        #         dp[(i, j)] = dfs(i + 1, j)

        #     return dp[(i, j)]


        # return dfs(0, 0)












        # dp = {}

        # def dfs(i, j):

        #     if len(t) == j:
        #         return 1
        #     if len(s) == i:
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]
        #     if s[i] == t[j]:
        #         dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
        #     else:
        #         dp[(i, j)] = dfs(i + 1, j)
        #     return dp[(i, j)]
        # return dfs(0, 0)
            
        