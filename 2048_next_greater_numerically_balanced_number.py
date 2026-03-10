from collections import defaultdict
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        """
        Decent approach to solve the question. Since we know the that constraint is 10^6, so we decided to check if n + 1 is balance or not we know that we wont have to go too far it is a correct way of doing it. Given by chatGpt, you can definately find a better solution.
        """
        
        def isbalanced(x):
            count = defaultdict(int)

            for i in str(x):
                count[i] += 1
            # print(count)
            for i in str(x):
                if int(i) != count[i]:
                    return False

            return True

        x = n + 1
        while True:

            if isbalanced(x):
                return x
            x += 1

            

        