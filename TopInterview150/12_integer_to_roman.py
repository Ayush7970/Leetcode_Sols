class Solution:
    def intToRoman(self, num: int) -> str:

        """
        Could not crack it try again 
        T.C -> O(n)
        S.C -> O(1)
        In this question we alter the table and add the 4's and 9's (that was basically one if condition and we eleminated a good amount of code with it) after that we just simply loop in descending order and make sure we store the values as we go. I could not solve it on my first go, so redo it if you visit it again.

        The tricky part was understanding that by including the 4's and 9's we eleminated the part was subtracting we can just multiple the the most left digit after extracting it and checking in hash table, we loop in descending order in hash table so we get 9 or 4 before any number that needs to be multiped but will alwasys be smaller then them, so we just take the quotient by divinding by 9 and multiply the literal with quotient that is 1 (if we divide 9 by 9).
        """

        roman = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]

        s= "" 

        for lit, val in reversed(roman):
            if num // val:
                print(num, val)
                ans = num // val
                print(ans)
                s += (lit * ans)
                num = num % val
        return s
