from collections import defaultdict
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        """
        One of the craziest and fun question. Definately solve it gain. I am proud I logically reached the aprt where I have to store a2 and b2 to get the a1 (just for cancelling out). But I did not know that we have to do it with graph. So that was the important part. It was not that intuitive.
        """

        adj = defaultdict(list)

        for i, val in enumerate(equations):
            a, b = val
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])
        
        def bfs(src, target):

            if src not in adj or target not in adj:
                return -1.0

            dq = deque([[src, 1]])
            visit= set()
            visit.add(src)

            while dq:
                val, w = dq.popleft()
                if target == val:
                    return w
    
                for n2, w2 in adj[val]:
                    if n2 not in visit:
                        visit.add(n2)
                        dq.append([n2, w * w2])
            
            return -1.0

        return [bfs(q1, q2) for q1, q2 in queries]


