class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


        """
        Dp optimized version
        T.C -> O(m * n), same as memoized version
        S.C -> O(m * n), same as memoized version
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        dp[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):

            for j in range(n - 1, -1, -1):

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i < m - 1:
                        dp[i][j] += dp[i + 1][j]
                    if j < n - 1:
                        dp[i][j] += dp[i][j + 1]

        return dp[0][0]


        """
        Pretty good question. This is the memoized version for it. Nothing too complex just handling the edge cases and time compliextiy. Make sure you undersrtadn how the memo dictionary actually works in it.
        T.C -> O(m * n)
        S.c -> O(m * n)
        """
        
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # count = [0]
        # memo = {}
        # def dfs(i, j):

        #     if i >= m or j >= n:
        #         return 0
        #     if obstacleGrid[i][j] == 1:
        #         return 0

        #     if i == m - 1 and j == n - 1:
        #         # count[0] += 1
        #         return 1
            
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
        #     return memo[(i, j)]

        # return dfs(0, 0)
        # # return count[0]

