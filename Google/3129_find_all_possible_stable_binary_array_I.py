from functools import lru_cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

        """
        Try Again
        One of the hardest question so far, In this question dfs was not passing time complexity requirement. The solution is bottom up programming approach. In which you build the table from the beginning.
        The intuition is if need dp[i][j][0] then it is actually the sum of dp[i - 1][j] where it is ending in zeros and dp[i - 1][j] and where it is ending in one, basically summing up all current possible comibnations because you will add zero in front of them(you are physically adding zeros). Once you sum up you keep on moving.
        Now of the trickest part is that when you exceed the limit you will have to subtract something, that something is the sum at dp[i - limit - 1][j][1], coz that will be the place where you know you have stored the total sum when zero would be upto the limit. 
        """
        mod = 10 ** 9 + 7
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]

        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1

        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1
        
        for i in range(1, zero + 1):
            for j in range(1, one + 1):

                if i > limit:
                    dp[i][j][0] = (
                        dp[i - 1][j][1] + dp[i - 1][j][0] - dp[i - limit - 1][j][1]
                    )
                else:
                    dp[i][j][0] = dp[i - 1][j][1] + dp[i - 1][j][0]
                dp[i][j][0] = (dp[i][j][0] % mod + mod) % mod

                if j > limit:
                    dp[i][j][1] = (
                        dp[i][j - 1][0] + dp[i][j - 1][1] - dp[i][j - limit - 1][0]
                    )
                else:
                    dp[i][j][1] = dp[i][j - 1][0] + dp[i][j - 1][1]
                dp[i][j][1] = (dp[i][j][1] % mod + mod) % mod

        return (dp[zero][one][0] + dp[zero][one][1]) % mod

            
                