class Solution:
    def totalNQueens(self, n: int) -> int:


        """
        Same as N queens I just one diffrence.
        DFS quesiton. Pretty important becuase you have to calculate the diags and vertical and horizontal moves. The correct way of understanding this questin. is think about how would you place the queens one by one in each row (NOT one by one in each col). This way oyu can understand you need DFS/ back track for each and every position to place the queen. So you go such as you place for row 0 to col 0 and then you go down check each pistion on other cols and then after completing that path you come back up and then you go col 1 of row 0 and the do everything. When you come back you have to remove the queens from board you placed and remove the values from sets by backtracking.
        """

        cols, pos_diag, neg_diag = set(), set(), set()

        res = [0]
        count = [0]
        def dfs(r):

            if r == n:
                count[0] += 1
                return 
            
            for c in range(n):
                if c in cols or r + c in pos_diag or r - c in neg_diag:
                    continue
                
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                res[0] += 1
                dfs(r + 1)

                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                res[0] -= 1

            
        dfs(0)
        return count[0]