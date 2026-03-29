from collections import Counter
class Solution:

    def countAndSay(self, n: int) -> str:
        """
        Simple string question. I used recursion to again and agian pass the evaluated string. The evaulation of the string was simple, you just have to add the number of times the string occured before each number.
        Improvement -> Use a array instead of a string, since strings are immutable, so when you write new_s += str(c), it creates a new string everytime, which increases time Complexity by O(n) and space complexity is not disturbed, since everytime only one string is alive.
        T.C -> O(2^n)
        S.C -> O(2^n)
        You could have done this question use iterative menthod as well, in which you simple replace the recurison with a for loop for an. 
        """

        def recur(count, s):

            if count == n:
                return s
            
            new_s = ""
            c = 1
            s += "-"
            for i in range(len(s) - 1):

                if s[i] != s[i + 1]:
                    new_s += str(c) + s[i]
                    c = 1
                else:
                    c += 1

            return recur(count + 1, new_s)

        return recur(1, "1")

            
        