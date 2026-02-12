
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        """
        Do it Again!
        Pretty Tough Array question. It was all about dealing with multiple edge cases. We basically first loop through the words, create the whole line list and then if we check with the if condition + adding the space, if that line is full. We simply add the spaces and then add it in the res. The beatiful and the important of this solution is that how edge cases for last line get perfectly set in the solution of Neetcode.
        """

        res, line, length = [], [], 0
        i = 0
        while i < len(words):

            if len(line) + length + len(words[i]) > maxWidth:

                extra_spaces = (maxWidth - length)
                spaces = extra_spaces // max(1, len(line) - 1) # -1 since there will one space less than the number of words
                rem = extra_spaces % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces

                    if rem:
                        line[j] += " "
                        rem -= 1
                
                res.append("".join(line))
                length, line = 0, []
            
            length += len(words[i])
            line.append(words[i])
            i += 1
        
        last_line = " ".join(line)
        extra_space = maxWidth - len(last_line)
        res.append(last_line + (extra_space * " "))
        return res
        







        