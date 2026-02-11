class Solution:
    def trailingZeroes(self, n: int) -> int:

        """
        Even better approach, read the one below 
        """

        count = 0
        multiple = 5
        while n >= multiple:
            count += n // multiple
            multiple *= 5
        
        return count


        """
        Simple Approach, I was very close to crack it but failed at creating the solution. The tricky part is that number of 5 will be calcualted twice when it is 25, as it is 2 5's itself. Morever, we wont count 2's since it will always be more than 5. 
        """
        # count = 0

        # for i in range(5, n + 1, 5):
        #     current = i
        #     while current % 5 == 0:
        #         count += 1
        #         current //= 5
            
        # return count 
            

        