def bellman_ford(n, edges, src):
    dist = [float("inf")] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Negative cycle detected")
            return None
    return dist

n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))
edges = []
for _ in range(m):
    u, v, w = map(int, input("Enter edge (u v w): ").split())
    edges.append((u, v, w))
src = int(input("Enter source vertex: "))

dist = bellman_ford(n, edges, src)
if dist:
    for i in range(n):
        print(f"Distance to {i}:", dist[i])
