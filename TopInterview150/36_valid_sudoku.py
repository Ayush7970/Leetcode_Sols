
from collections import defaultdict

class Solution:
    """
    Practice 1
    one important part in this question was to remember that you can use set inside dict values, you dont have to use list, since when you sue keyword in it will take O(n) time complexity while set will take O(1)
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        dict_row, dict_col, dict_box = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(ROWS):
            for j in range(COLS):
                value = board[i][j]
                if (value in dict_row[i] or value in dict_col[j] or value in dict_box[(i // 3, j // 3)]) and value != ".":
                    return False
                dict_row[i].add(value)
                dict_col[j].add(value)
                dict_box[(i // 3, j // 3)].add(value)
        return True

















        # ROWS = len(board)
        # COLS = len(board)

        # hash_rows = defaultdict(set)
        # hash_cols = defaultdict(set)
        # hash_block = defaultdict(set)


        # for i in range(ROWS):

        #     for j in range(COLS):

        #         if board[i][j] == ".":
        #             continue
        #         else:
        #             if board[i][j] not in hash_rows[i]:
        #                 hash_rows[i].add(board[i][j])
        #             else:
        #                 # print(board[i][j], "1")
        #                 return False
        #             if board[i][j] not in hash_cols[j]:
        #                 hash_cols[j].add(board[i][j])
        #             else:
        #                 # print(board[i][j], "2")
        #                 return False
        #             if board[i][j] not in hash_block[(i // 3, j // 3)]:
        #                 hash_block[(i // 3, j // 3)].add(board[i][j])
        #             else:
        #                 # print(hash_block[(block_i, block_j)])
        #                 # print(block_i, block_j)
                        
        #                 # print(board[i][j], "index", i,j ,"    ", "3")
        #                 return False
        
        # return True
                
                



















        # row = defaultdict(set)
        # col = defaultdict(set)
        # square = defaultdict(set)
        # for i in range(len(board)):
        #     for j in range(len(board)):
        #         if board[i][j] == ".":
        #             continue
        #         if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in square[(i // 3, j // 3)]:
        #             print(board[i][j])
        #             return False
        #         row[i].add(board[i][j])
        #         col[j].add(board[i][j])
        #         square[(i // 3, j // 3)].add(board[i][j])
        # return True


        