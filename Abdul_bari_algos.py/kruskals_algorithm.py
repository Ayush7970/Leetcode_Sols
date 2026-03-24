

"""
THis is Kruskals Algorithm in which we get greedy and simply find the two least weight edge and keep
on combining till we have n - 1 edges. We use Union find in this to prevent to form cycle and
more optimized version is to form path compression.
"""
class DSU:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   #path compression
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False
        
        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        elif self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_y] = parent_x
            self.rank[parent_x] += 1
        
        return True


def kruskals_algorithm(n, edges):

    edges.sort(key=lambda x: x[2])
    
    dsu = DSU(n)
    mst_cost = 0
    mst_edges = []

    for u, v, w in edges:

        if dsu.union(u, v):
            mst_edges.append((u, v, w))
            mst_cost += w
        
        if len(mst_edges) == n - 1:
            break
    
    if len(mst_edges) != n - 1:
        return None, []
    
    return mst_cost, mst_edges



n = 5
edges = [
    (0, 1, 2),
    (0, 4, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

cost, mst = kruskals_algorithm(n, edges)

print("MST Cost:", cost)
print("MST Edges:", mst)