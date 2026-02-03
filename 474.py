from collections import defaultdict
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        """
        YOU HAVE A GOLDEN RULE IN THIS!
        Knap sack 0/1 bottom up approach, the golden rule here is if you are compressiong the i away in the table then you are updating the table in the same state then you should loop backwad to prevent updating in the same state like dp[j][k] =max(dp[j][k], 1 + dp[j - z][ k - o]). Looking backward would prevent it. Morover, if you not compressing then you cna loop forward. ALWAYS REMEMBER THIS RULE.
        """

        dp = [[0] * (n +1) for _ in range(m + 1)]

        for s in strs:
            z = s.count("0")
            o = s.count("1")

            for j in range(m, z - 1, -1):
                for k in range(n, o - 1, -1):
                    dp[j][k] = max(dp[j][k], 1 + dp[j - z][ k - o])
            
        return dp[m][n]

        """
        Thi sis Knapsack 0/1 patterrn with memoized technique. In this the toguh part was to understand that (i, curr_m, curr_n) are in dict as a  tuple as a table because all three are moving indexes that can alter the ouptput, that is how you have to decide the memo table. 
        T.C -> O(n * m * len(strs))
        S.C -> O(n * m * len(strs))
        """
         
        # # dp = [ for _ in range(len(strs) + 1)]
        # dp = {}
        # def dfs(i, curr_m, curr_n):

        #     if i >= len(strs):
        #         return 0
            
        #     if (i, curr_m, curr_n) in dp:
        #         return dp[(i, curr_m, curr_n)]
            
        #     dp[(i, curr_m, curr_n)] = dfs(i + 1, curr_m, curr_n)

        #     m2 = strs[i].count("0")
        #     # print(curr_m, strs[i], strs[i].count("0"))
        #     n2 = strs[i].count("1")

        #     if curr_m - m2 >= 0 and curr_n - n2 >= 0:
        #         dp[(i, curr_m, curr_n)] = max(dp[(i, curr_m, curr_n)], 1 + dfs(i + 1, curr_m -m2, curr_n - n2))

        #     return dp[(i, curr_m, curr_n)]

        # return dfs(0, m, n)
