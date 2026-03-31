class Solution:
    def numTrees(self, n: int) -> int:

        """
        Dynmaic prgramming solution
        Preety Good question, we solved it through dp. For example, in each BST we make each and every node the root adn then we calculate the result for the left and right trees which should already be stored in the dp(since they will be smaller and already computed).
        The tricky part wass that if 3 is the root and the left tree will have only 2 nodes 1 and 2. and the right tree will have number of nodes in current BST - root.
        T.C -> O(n^2)
        S.C -> O(n)
        """

        dp = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1 # for example if 3 is root and then 2 nodes on left 2 and 1
                right = nodes - root
                total += dp[left] * dp[right]
            dp[nodes] = total
        
        return dp[n]

        # """
        # Formula for unique binary trees -> (2n)!/((1 + n)!*n!) but you can't d it simple multiplying so you cna use this formula:
        # C = C * 2 *(2 * i + 1) // (i + 2)
        # """
        # # solution usign formula 

        # C = 1
        # for i in range(n):
        #     C = C * 2 *(2 * i + 1) // (i + 2)
        
        # return C






    #     dp = [0] * (n + 1)

    #     def dfs(node):
    #         if node == 1:
    #             return 1
    #         if node == 0:
    #             return 1

    #         if dp[node] != 0:
    #             return dp[node]
    #         for root in range(1, node + 1):
    #             sum_left = dfs(root - 1)
    #             sum_right = dfs(node - root)
    #             dp[node] += sum_left * sum_right      
    #         return dp[node]
    #     return dfs(n)
        
