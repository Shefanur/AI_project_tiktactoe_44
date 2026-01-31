graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

h = {'A':5, 'B':4, 'C':3, 'D':1, 'E':2, 'F':0}

def Greedy(graph, source, h):
    frontier = [source]
    visited = set()
    parent = {source: None}
    tree_edges = []
    order = []

    print(f"Starting Greedy Best-First Search from {source}\n")

    while frontier:
        # select node with smallest heuristic
        frontier.sort(key=lambda x: h[x])
        u = frontier.pop(0)
        if u in visited:
            continue

        visited.add(u)
        order.append(u)
        print(f"Expanding Node: {u} (h = {h[u]})")

        for v in graph[u]:
            if v not in visited:
                parent[v] = u
                tree_edges.append((u, v))
                frontier.append(v)
                print(f"  Added to frontier: {v} (parent: {u})")

    # Final Output
    print("\nGreedy Best-First Parent Table:")
    for n in order:
        print(f"{n} <-- {parent[n]}")

    print("\nGreedy Tree Edges:")
    for u,v in tree_edges:
        print(f"{u} -> {v}")

    print("\nMain Output (Node Expansion Order):", " ".join(order))

# Run Greedy Best-First Search
Greedy(graph, 'A', h)