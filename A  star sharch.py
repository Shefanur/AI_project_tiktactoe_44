def A_star(graph, cost, h, start, goal):
    open_list = {start}
    closed_list = set()
    g = {start: 0}
    parent = {start: None}
    tree_edges = []
    order = []

    while open_list:
        current = min(open_list, key=lambda x: g[x]+h[x])
        order.append(current)
        if current == goal:
            break
        open_list.remove(current)
        closed_list.add(current)

        for neigh in graph[current]:
            temp_g = g[current]+cost[(current, neigh)]
            if neigh not in open_list and neigh not in closed_list:
                open_list.add(neigh)
                parent[neigh] = current
                tree_edges.append((current, neigh))
                g[neigh] = temp_g
            elif temp_g < g.get(neigh, float("inf")):
                g[neigh] = temp_g
                parent[neigh] = current
                if neigh in closed_list:
                    closed_list.remove(neigh)
                    open_list.add(neigh)

    print("A* Parent Table:")
    for n in parent: print(f"{n} <-- {parent[n]}")
    print("\nA* Tree Edges:")
    for u,v in tree_edges: print(f"{u} -> {v}")
    print("\nMain Output:", " ".join(order))

# Example
graph = {'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':['F'],'F':[]}
cost = {('A','B'):1,('A','C'):4,('B','D'):2,('B','E'):5,('C','F'):3,('E','F'):1}
h = {'A':6,'B':4,'C':3,'D':4,'E':2,'F':0}

A_star(graph, cost, h, 'A', 'F')