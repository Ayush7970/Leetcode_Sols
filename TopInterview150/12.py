class Solution:
    def intToRoman(self, num: int) -> str:

        """
        In this question we alter the table and add the 4's and 9's (that was basically one if condition and we eleminated a good amount of code with it) after that we just simply loop in descending order and make sure we store the values as we go. I could not solve it on my first go, so redo it if you visit it again.
        """

        roman = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]

        s = ""
        for sym, val in reversed(roman):
            if num // val:
                ans = num // val
                s += (sym * ans)
                num = num % val

        return s
