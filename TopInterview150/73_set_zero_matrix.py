class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        """
        The tricky part was to upgrade in place. The best way to do it to use the first value of row and col to use as a flag and then upgrade them as well in the end seperately. Morever, the tricky part is also matrix[0][0] since we nedd to check for col 0 and row 0. Therefore, we takke an additional variable zero_col and we turn True if col zero has even one zero. 
        """

        zero_col = False
        R = len(matrix)
        C = len(matrix[0])

        for i in range(R):
            if matrix[i][0] == 0:
                zero_col = True
            for j in range(1, C):

                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
            
        for i in range(1, R):
            for j in range(1, C):

                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if not matrix[0][0]:
            for j in range(C):
                matrix[0][j] = 0
                
        if zero_col:
            for i in range(R):
                matrix[i][0] = 0
            
        
        
        return 

        




        # col0 = True
        # rows = len(matrix)
        # cols = len(matrix[0])

        # for r in range(rows):
        #     for c in range(cols):
        #         if matrix[r][c] == 0:
        #             matrix[0][c] = 0
        #             if r > 0:
        #                 matrix[r][0] = 0
        #             else:
        #                 col0 = 0
        
        # for r in range(1, rows):
        #     for c in range(1, cols):
        #         if matrix[0][c] == 0 or matrix[r][0] == 0:
        #             matrix[r][c] = 0
        
        # if matrix[0][0] == 0:
        #     for r in range(rows):
        #         matrix[r][0] = 0

        # if col0 == 0:
        #     for c in range(cols):
        #         matrix[0][c] = 0








        # # col0 = 1
        # # for i in range(len(matrix)):
        # #     for j in range(len(matrix[0])):
        # #         if matrix[i][j] == 0:
        # #             matrix[i][0] = 0
        # #             if j == 0:
        # #                 col0 = 0
        # #             else:
        # #                 matrix[0][j] = 0
        
        
        # # for i in range(1, len(matrix)):
        # #     for j in range(1, len(matrix[0])):
        # #         if matrix[0][j] == 0 or matrix[i][0] == 0:
        # #             matrix[i][j] = 0
        
        
        # # if matrix[0][0] == 0:
            
        # #     for i in range(len(matrix[0])):
        # #         matrix[0][i] = 0

        # # if col0 == 0:
        # #     for i in range(len(matrix)):
        # #         matrix[i][0] = 0

        



        
        
        
        