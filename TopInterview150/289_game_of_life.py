
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        arr = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        """
        Better Approach, in this space complexity is O(1). Since we are doing in place traversal. We simply change the died cell rto -1 instead of 0 and cell which were dead to 2. Note we do not change the cell which were ones and stayed alive. At the end we traverse again and replace those values.
        """
        def count_func(i, j):
            count = 0
            for x, y in arr:
                if i + x >= 0 and i + x < len(board) and j + y >= 0 and j + y < len(board[0]) and (board[i + x][j + y] == 1 or board[i + x][j + y] == -1):
                    count += 1

            return count

        for i in range(len(board)):

            for j in range(len(board[0])):

                count = count_func(i, j)
                if board[i][j] == 1 and count < 2:
                    board[i][j] = -1
                elif board[i][j] == 1 and (count == 2 or count == 3):
                    board[i][j] = 1
                elif board[i][j] == 1 and count > 3:
                    board[i][j] = -1
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 2
                print(board[i][j])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0



        