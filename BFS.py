from collections import deque

def BFS(graph, source):
    parent = {source: None}
    tree_edges = []
    order = []
    visited = set([source])
    q = deque([source])

    while q:
        u = q.popleft()
        order.append(u)

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                tree_edges.append((u, v))
                q.append(v)

    print("BFS Parent Table:")
    for node in parent:
        print(f"{node} <-- {parent[node]}")

    print("\nBFS Tree Edges:")
    for u, v in tree_edges:
        print(f"{u} -> {v}")

    print("\nMain Output:", " ".join(order))


graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

BFS(graph, 'A')