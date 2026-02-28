class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:


        """
        Practice 1, could not solve it in practice 1 as well try it again
        """

        dp = {}


        def dfs(r, c):
            if r >= len(matrix) or c >= len(matrix[0]):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            else:
                down = dfs(r, c + 1)
                right = dfs(r + 1, c)
                diagonal = dfs(r + 1, c + 1)

                dp[(r, c)] = 0
                if matrix[r][c] == "1":
                    dp[(r,  c)] = 1 + min(down, right, diagonal)
                
                return dp[(r, c)]
 



        dfs(0, 0)
        answer = max(dp.values())
        return answer * answer





    #     ROWS = len(matrix)
    #     COLS = len(matrix[0])

    #     dp = {}

    #     def dfs(r, c):
    #         if r > ROWS - 1 or c > COLS - 1:
    #             return 0
    #         if (r, c) in dp:
    #             return dp[(r, c)]
    #         else:
    #             down = dfs(r + 1, c)
    #             right = dfs(r, c + 1)
    #             diagonal = dfs(r + 1, c + 1)

    #             dp[(r, c)] = 0
    #             if matrix[r][c] == "1":
    #                 dp[(r, c)] = 1 + min(down, right, diagonal)
            
    #             return dp[(r, c)]
            
    #     dfs(0, 0)

    #     answer = max(dp.values())
    #     return answer * answer