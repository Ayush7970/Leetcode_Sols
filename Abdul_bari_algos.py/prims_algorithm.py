
import heapq

"""
This is Prim's Algorithm in which we find the minimum spanning tree, we use a min_heap and adjacency list
min_heap helps to get the minimum weight everytime we choose the nearest neighbour to move forward.
"""

def prims_algorithm(n, edges):

    graph = {i: [] for i in range(n)}

    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    visited = set()
    min_heap = [] 
    mst_cost = 0
    mst_edges = []

    visited.add(0)
    for weight, neighbour in graph[0]:
        heapq.heappush(min_heap, (weight, 0, neighbour))
    

    while min_heap and len(visited) < n:     # two conditions for while loop imp!
        curr_weight, start, end = heapq.heappop(min_heap)

        if end in visited:
            continue

        visited.add(end)

        mst_cost += curr_weight
        mst_edges.append((start, end, weight))

        for next_weight, next_node in graph[end]:
            if next_node not in visited:
                heapq.heappush(min_heap, (next_weight, end, next_node))
    

    if len(visited) != n:
        return None, []
    
    return mst_cost, mst_edges


n = 5
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

cost, mst = prims_algorithm(n, edges)

print("MST Cost:", cost)
print("MST Edges:", mst)
