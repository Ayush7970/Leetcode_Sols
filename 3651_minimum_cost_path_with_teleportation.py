
class Solution:

    """
    TRAIL 1: Do again!
    WORK ON INTUITION MORE NEXT TIME.
    Craziest 1st hard leetcode, In this problem you can either mvoe right or down or teleprot to <= values. Therefore you first ahve to create a algorithm for teleportation and then you aso ahve to take care of the DP. You do DP again and agian because you can practically do some telport then move right or down then. some telelport and then some right and down. 

    You sort the points which is the indexing of the table (you sort it by grid value). What you do at each step all the values that are <= you store the minCost in all of them and then you again do the dp and then you agian do teleport. The first loop, is basically the number of the times you can teleport. 
    """
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        points = [(i, j) for i in range(m) for j in range(n)]
        costs = [[float("inf")] * n for i in range(m)]
        points.sort(key=lambda p: grid[p[0]][p[1]])
        print(points)
        for t in range(k + 1):

            minCost= float("inf")
            j = 0
            for i in range(len(points)):
                # print(i)
                minCost = min(minCost, costs[points[i][0]][points[i][1]])
                if i + 1 < len(points) and grid[points[i][0]][points[i][1]] == grid[points[i + 1][0]][points[i + 1][1]]:
                    i += 1
                    continue
                for r in range(j, i + 1):
                    costs[points[r][0]][points[r][1]] = minCost
                j = i + 1

            for i in range(m - 1, -1, -1):

                for j in range(n - 1, -1, -1):

                    if i == m - 1 and j == n - 1:
                        costs[i][j] = 0
                        continue
                    if i != m - 1:
                        costs[i][j] = min(costs[i][j], costs[i + 1][j] + grid[i + 1][j])

                    if j != n - 1:
                        costs[i][j] = min(costs[i][j], costs[i][j + 1] + grid[i][j + 1])
        return costs[0][0]

