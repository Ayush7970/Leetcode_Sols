from ast import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        """ Matrix type question. In this question, the hard part was to do it in place, for that we realized that first we move all the for corners. This way we only need one extra space and then we keep on move 1 step forward from the corners to cover those rows (which is our for loop). Whereas, in the while then we reduce the space, which lets us move through the inner square by doing l += 1 and r -= 1. This is the stratergy to deal with O(1) space complexity. Otherwise, it is too easy since you just have to create a formaula to take the value and store it in another matrix.
        """
        l, r = 0, len(matrix) - 1

        while l < r:

            for i in range(r - l):

                top, bottom = l, r

                new_top_left = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = matrix[top][l + i]
                matrix[top][l + i] = new_top_left

            l += 1
            r -= 1
        

                






















        
        # l, r = 0 , len(matrix) - 1
        # while l <= r:

        #     for i in range(r - l):

        #         top, bottom = l , r

        #         topleft = matrix[top][l + i]

        #         matrix[top][l + i] = matrix[bottom - i][l]

        #         matrix[bottom- i][l] = matrix[bottom][r - i]

        #         matrix[bottom][r - i] = matrix[top + i][r]

        #         matrix[top + i][r] = topleft
            
        #     l += 1
        #     r -= 1
        
        # return matrix



        

















        
        # for i in range(len(matrix)-1):
        #     for j in range(i+1, len(matrix)):
        #         t = matrix[i][j]
        #         matrix[i][j] = matrix[j][i]
        #         matrix[j][i] = t
        
        # for i in range(len(matrix)):
        #     matrix[i] = reversed(matrix[i])

                

        