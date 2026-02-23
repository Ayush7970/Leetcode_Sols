class Solution:
    def reverseWords(self, s: str) -> str:

        """
        Simple string type word extraction
        """

        res = ""
        i = 0
        word = ""
        s += " "
        while i < len(s):

            if s[i] == " ":
                if word:
                    res = word + " " + res if res else word
                word = ""
            else:
                word += s[i] 

            i += 1
        return res










        # temp = ""
        # reverse = ""
        # index = 0
        # while index < len(s):
        #     if s[index] != ' ':
        #         temp += s[index]
        #         # print("2", temp, "2")
        #     elif s[index] == ' ':
        #         if temp != "":
        #             if reverse == "":
        #                 reverse = temp
        #                 print(reverse, "reverse1")
        #             else:
        #                 reverse = temp + " " + reverse
        #             temp = ""
        #     index += 1

        # if temp != "":
        #     if reverse == "":
        #         reverse = temp
        #     else:
        #         reverse = temp + " " + reverse
        # return reverse
        

