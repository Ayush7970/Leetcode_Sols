class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        """
        Insane Crazy greedy solution. I could not solve it on the first go. The hard part is where to start looping twice and checking again is easy, till that position. However, NEetcode solution is more crazy, he basically eleminated all the -1 cases (in which) in the first edge case. Then there is definately either one solution or not. Therefore, it is a crazy solution that you dont even need to loop again.
        """
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):

            total += gas[i] - cost[i]
            if total < 0:
                start = i + 1
                total = 0
            
        return start
        









        # if sum(gas) < sum(cost):
        #     return -1
        # start = 0
        # total = 0
        # for i in range(len(gas)):
        #     total += (gas[i] - cost[i])
        #     if total < 0:
        #         total = 0
        #         start = i + 1
        # return start
        