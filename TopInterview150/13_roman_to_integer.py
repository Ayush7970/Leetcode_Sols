class Solution:
    def romanToInt(self, s: str) -> int:
        
        """
        T.C -> O(n)
        S.C -> O(1)
        Try it agian could not solve it. 
        It was a easy question, you just have to understand what are all the cases, which are two either you plus or subtract, since you know when to subtract you just have to create cases for it. Which is if the value is less than the next value then we will subtract it, other will get added even it is VI, it will addded idvidually so not a problem.
        """

        dict1 = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        total = dict1.get(s[-1])
        for i in range(len(s) - 1):

            if i + 1 < len(s) and dict1[s[i]] < dict1[s[i + 1]]:
                total -= dict1[s[i]]
            else:
                total += dict1[s[i]]
        
        return total


        


        
        
        