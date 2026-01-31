
   graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def DFS(graph, source):
    parent = {source: None}  # parent table
    tree_edges = []           # edges in DFS tree
    order = []                # traversal order
    visited = set()           # visited nodes

    def dfs(u):
        visited.add(u)
        order.append(u)       # add current node to traversal
        for v in graph[u]:
            if v not in visited:
                parent[v] = u
                tree_edges.append((u, v))
                dfs(v)

    dfs(source)

    # Print DFS Parent Table
    print("DFS Parent Table:")
    for node in order:
        print(f"{node} <-- {parent[node]}")

    # Print DFS Tree Edges
    print("\nDFS Tree Edges:")
    for u, v in tree_edges:
        print(f"{u} -> {v}")

    # Print Main Output (DFS traversal order)
    print("\nMain Output:", " ".join(order))

# Run DFS
DFS(graph, 'A')