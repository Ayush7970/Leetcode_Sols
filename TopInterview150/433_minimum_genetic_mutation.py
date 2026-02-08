from collections import deque
from typing import List
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        """
        This question was a BFS question. The importnat aprt for these quesitons are you ahv eto find the shortest path to the closest end string, for that you should use BFS, since BFS is good for shortest path over DFS. Then, the important part was that how you will identify the next neighbour. For that you ahve to check all possible sequence by changing each character with AGCT. This will be the modification you are supposed to in BFS for this question.
        """

        dq = deque([(startGene, 0)])
        visit = set([startGene])

        while dq:
            node, steps = dq.popleft()

            if node == endGene:
                return steps
            
            for ch in "ACGT":
                for i in range(len(node)):
                    neighbour = node[:i] + ch + node[i + 1:]
                    if neighbour in bank and neighbour not in visit:
                        dq.append((neighbour, steps + 1))
                        visit.add(neighbour)
            
        return -1
    



       

        

        