graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def DLS(graph, node, depth, visited, parent, tree_edges, order):
    if depth < 0:
        return
    visited.add(node)
    order.append(node)
    for v in graph[node]:
        if v not in visited:
            parent[v] = node
            tree_edges.append((node, v))
            DLS(graph, v, depth-1, visited, parent, tree_edges, order)

def IDS(graph, source, max_depth=5):
    print(f"Starting Iterative Deepening Search from {source}\n")
    for depth in range(max_depth):
        visited = set()
        parent = {source: None}
        tree_edges = []
        order = []

        DLS(graph, source, depth, visited, parent, tree_edges, order)

        # If all nodes visited, print results
        if len(order) == len(graph):
            print("IDS Parent Table:")
            for n in order:
                print(f"{n} <-- {parent[n]}")

            print("\nIDS Tree Edges:")
            for u,v in tree_edges:
                print(f"{u} -> {v}")

            print("\nMain Output (Node Expansion Order):", " ".join(order))
            return

IDS(graph, 'A')