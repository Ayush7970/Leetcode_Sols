import heapq

"""
Dijkstra's Algo time complexity is O(elogV) if you use a min heap and adjancency list otherwise O(V^2) if you use an adjacency matrix and linear search for the minimum distance.
Space Complexity is O(V+ E) for the graph and O(V) for the distance array and O(V) for the min heap in worst case, so overall O(V+E).
"""
def dijkstra(n, edges, source):

    graph =  {i : [] for i in range(n)}             # we create the graph

    for u, v, w in edges:
        graph[u].append((v, w))
    
    dist = [float("inf")] * n
    dist[source] = 0

    min_heap = [(0, source)]

    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)

        if curr_dist > dist[node]:          # if the distance in the dist array is already short then we dont have to take this path to that node
            continue

        for next_node, new_dist in graph[node]:

            if curr_dist + new_dist < dist[next_node]:
                dist[next_node] = curr_dist + new_dist
                heapq.heappush(min_heap, (curr_dist + new_dist, next_node))         # we store only those nodes for which we upgraded the path
    
    return dist



n = 5
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (3, 4, 3)
]
source = 0
print(dijkstra(n, edges, source))