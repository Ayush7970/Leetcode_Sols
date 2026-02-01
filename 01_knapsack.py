class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # lets do tabular approach 
        dp = [[0] * (capacity + 1) for _ in range(len(profit)) ]

        for i in range(len(profit)): dp[i][0] = 0

        for i in range(capacity + 1):
            if weight[0] <= i:
                dp[0][i] = profit[0]

        
        for i in range(1, len(profit)):
            for c in range(1, capacity + 1):
                skip = dp[i - 1][c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i - 1][c - weight[i]]
                dp[i][c] = max(skip, include)
        
        return dp[len(profit) - 1][capacity]

           
        
        # print(dp)
        # cache = [ ([-1] * (capacity + 1)) for i in range(len(profit))]
    
        # def recursive_func(iterator, current_capacity, cache):
        #     if iterator >= len(profit):
        #         return 0
            
        #     # print("iterator", iterator)
            
        #     if cache[iterator][current_capacity] != -1:
        #         return cache[iterator][current_capacity]
        #     # skipping

        #     cache[iterator][current_capacity] = recursive_func(iterator + 1, current_capacity, cache)

        #     # including
        #     if current_capacity - weight[iterator] >= 0:
                
        #         p = profit[iterator] + recursive_func(iterator + 1, current_capacity - weight[iterator], cache)
        #         cache[iterator][current_capacity] = max(cache[iterator][current_capacity], p)

        #         # print(iterator, current_capacity, cache[iterator][current_capacity])
        #     print(iterator, current_capacity)
        #     return cache[iterator][current_capacity]

        # return recursive_func(0, capacity, cache)



