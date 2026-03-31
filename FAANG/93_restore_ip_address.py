class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        """
        Try Again.
        This was a good backtrack/recursion question. In which you basically did not do any backtracking. YOu basically have to place the dots correctly so we used a for loop to place dots upto three characters as more will not be possible. THe tricky part was to deal with the leasding zeros (if i == j means single digit zero is valid ese s[i] != 0 means firsst digit cannot be zero). 
        I could not figure out the for loop in the recursion. Always try to create decision tree first. For these type of questions!
        T.C -> O(3^4) which should Ibe constant so O(1)
        S.C -> O(1) 
        since max depth is 4
        """

        res = []
        def backtrack(i, dots, curr_ip):

            if dots == 4 and i == len(s):
                res.append(curr_ip[:-1])
                return

            if dots > 4:
                return

            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j + 1, dots + 1, curr_ip + s[i:j + 1] + ".")

        backtrack(0, 0, "")
        return res

