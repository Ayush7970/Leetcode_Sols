class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        """
        DFS quesiton. Pretty important becuase you have to calculate the diags and vertical and horizontal moves. The correct way of understanding this questin. is think about how would you place the queens one by one in each row (NOT one by one in each col). This way oyu can understand you need DFS/ back track for each and every position to place the queen. So you go such as you place for row 0 to col 0 and then you go down check each pistion on other cols and then after completing that path you come back up and then you go col 1 of row 0 and the do everything. When you come back you have to remove the queens from board you placed and remove the values from sets by backtracking.
        """

        board = [["."] * n for i in range(n)]

        cols, pos_diag, neg_diag = set(), set(), set()
        res= []
        def dfs(row):

            if row == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in cols or row + c in pos_diag or row - c in neg_diag:
                    continue

                cols.add(c)
                pos_diag.add(row + c)
                neg_diag.add(row - c)
                board[row][c] = 'Q'

                dfs(row + 1)

                cols.remove(c)
                pos_diag.remove(row + c)
                neg_diag.remove(row - c)
                board[row][c] = '.'

        dfs(0)
        return res































        # cols = set()
        # posdiags = set()
        # negdiags = set()
        # res = []
        # board = [(["."] * n) for i in range(n)]


        # def dfs(r):
        #     if r == n: 
        #         copy = ["".join(row) for row in board]
        #         res.append(copy)
        #         return

        #     for c in range(n):
        #         if c in cols or r + c in posdiags or r - c in negdiags:
        #             continue
        #         board[r][c] = "Q"
        #         cols.add(c)
        #         posdiags.add(r + c)
        #         negdiags.add(r - c)

        #         dfs(r + 1)

        #         board[r][c] = "."
        #         cols.remove(c)
        #         posdiags.remove(r + c)
        #         negdiags.remove(r - c)
        
        # dfs(0)
        # return res
            


            
        













        # cols = set()
        # posdiag = set()
        # negdiag = set()
        # res = []
        # board = [["."] * n for i in range(n)]

        # def backtrack(r):
        #     if r == n:
        #         copy = ["".join(row) for row in board]
        #         res.append(copy)
        #         return
            
        #     for c in range(n):
        #         if c in cols or (r+c) in posdiag or (r-c) in negdiag:
        #             continue
        #         cols.add(c)
        #         posdiag.add(r+c)
        #         negdiag.add(r-c)
        #         board[r][c] = "Q"

        #         backtrack(r+1)

        #         cols.remove(c)
        #         posdiag.remove(r+c)
        #         negdiag.remove(r-c)
        #         board[r][c] = "."
        
        # backtrack(0)
        # return res
            







        